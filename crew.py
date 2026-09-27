from crewai import Crew, Process, Task

from agent import create_tutor


def create_tutor_crew():
    tutor = create_tutor()

    task = Task(
        description="""
Tutor the student.

Subject:
{subject}

Study mode:
{study_mode}

Student question:
{question}

Previous conversation:
{conversation}

Give a clear and educational response.

Use the calculator when calculations are required.
Use study material search when useful.
Focus on helping the student understand.
""",
        expected_output="""
A clear, accurate and student-friendly tutoring response.
""",
        agent=tutor,
    )

    return Crew(
        agents=[tutor],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )
