import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_secret(name):
    """Get a secret from Streamlit Cloud Secrets or environment variables."""

    try:
        value = st.secrets.get(name)

        if value:
            return value
    except Exception:
        pass

    return os.getenv(name)


# API keys
GROQ_API_KEY = get_secret("GROQ_API_KEY")
TAVILY_API_KEY = get_secret("TAVILY_API_KEY")

# AI model
MODEL_NAME = "groq/openai/gpt-oss-120b"


def validate_settings():
    """Make sure all required API keys are available."""

    missing = []

    if not GROQ_API_KEY:
        missing.append("GROQ_API_KEY")

    if not TAVILY_API_KEY:
        missing.append("TAVILY_API_KEY")

    if missing:
        raise RuntimeError(
            "Missing environment variables: "
            + ", ".join(missing)
        )
