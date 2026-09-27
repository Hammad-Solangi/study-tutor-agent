from crewai import Agent, LLM

from settings import MODEL_NAME, GROQ_API_KEY
from prompts import (
    TUTOR_ROLE,
    TUTOR_GOAL,
    TUTOR_BACKSTORY,
)
from tools import calculator, study_material_search


def create_tutor():
    llm = LLM(
    model=MODEL_NAME,
    temperature=0.3,
    api_key=GROQ_API_KEY,
)
    return Agent(
        role=TUTOR_ROLE,
        goal=TUTOR_GOAL,
        backstory=TUTOR_BACKSTORY,
        llm=llm,
        tools=[
            calculator,
            study_material_search,
        ],
        allow_delegation=False,
        verbose=True,
    )
