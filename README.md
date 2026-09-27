# 📚 Study Tutor Agent

A modular AI study tutor built with:

- Streamlit
- CrewAI
- GPT-OSS-120B
- Groq
- Tavily

## Features

- AI tutoring
- Multiple subjects
- Multiple study modes
- Calculator tool
- Study material search
- Conversation memory

## Tools

### Calculator
Used for numerical calculations.

### Study Material Search
Searches for educational material using Tavily.

## Environment Variables

The application requires:

- `GROQ_API_KEY`
- `TAVILY_API_KEY`

Add these as environment variables in Render.

Never commit real API keys to GitHub.

## Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```
