import streamlit as st

from settings import validate_settings
from crew import create_tutor_crew
from memory import build_conversation

st.set_page_config(
    page_title="Study Tutor",
    page_icon="📚",
    layout="centered",
)

try:
    validate_settings()
except RuntimeError as error:
    st.error(str(error))
    st.stop()

st.title("📚 Study Tutor")
st.caption("Your personal AI study tutor")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Study Settings")

    subject = st.selectbox(
        "Subject",
        [
            "General",
            "Physics",
            "Mathematics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "English",
        ],
    )

    study_mode = st.selectbox(
        "Study Mode",
        [
            "Learn",
            "Solve",
            "Explain Simply",
            "Quiz",
            "Exam Practice",
        ],
    )

    st.divider()

    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your tutor...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    conversation = build_conversation(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Your tutor is thinking..."):
            try:
                tutor_crew = create_tutor_crew()

                result = tutor_crew.kickoff(
                    inputs={
                        "question": question,
                        "subject": subject,
                        "study_mode": study_mode,
                        "conversation": conversation,
                    }
                )

                response = str(result)

            except Exception as error:
                response = f"Something went wrong.\n\n`{error}`"

        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
