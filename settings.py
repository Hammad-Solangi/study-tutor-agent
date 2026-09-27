import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = "groq/openai/gpt-oss-120b"


def validate_settings():
    missing = []

    if not GROQ_API_KEY:
        missing.append("GROQ_API_KEY")

    if not TAVILY_API_KEY:
        missing.append("TAVILY_API_KEY")

    if missing:
        raise RuntimeError(
            "Missing environment variables: " + ", ".join(missing)
        )
