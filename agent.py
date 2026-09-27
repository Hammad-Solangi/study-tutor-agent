from crewai import Agent
from groq_llm import GroqLLM

from settings import MODEL_NAME, GROQ_API_KEY
from prompts import (
    TUTOR_ROLE,
    TUTOR_GOAL,
    TUTOR_BACKSTORY,
)
from tools import calculator, study_material_search


def create_tutor():
   llm = GroqLLM(
    model=MODEL_NAME,
    temperature=0.3,
    api_key=GROQ_API_KEY,
    max_tokens=1000,
)
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
