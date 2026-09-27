import os
import requests

from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    allowed_characters = set("0123456789+-*/().% ")

    if not all(
        character in allowed_characters
        for character in expression
    ):
        return "Invalid mathematical expression."

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )
        return str(result)

    except Exception as error:
        return f"Calculation error: {error}"


@tool("Study Material Search")
def study_material_search(query: str) -> str:
    """Search the web for educational study material."""

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return "Study material search is not configured."

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": api_key,
                "query": f"{query} educational study material",
                "search_depth": "basic",
                "max_results": 5,
            },
            timeout=15,
        )

        response.raise_for_status()
        data = response.json()

        results = []

        for result in data.get("results", []):
            results.append(
                f"""
Title: {result.get("title", "")}

URL: {result.get("url", "")}

Content:
{result.get("content", "")}
"""
            )

        if not results:
            return "No useful study material was found."

        return "\n---\n".join(results)

    except Exception as error:
        return f"Study search failed: {error}"
