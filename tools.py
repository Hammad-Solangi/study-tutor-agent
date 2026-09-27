import requests
from crewai.tools import tool

from settings import TAVILY_API_KEY


@tool("Calculator")
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    allowed_characters = set(
        "0123456789+-*/().% "
    )

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
    """Search the web for educational study material using Tavily."""

    if not TAVILY_API_KEY:
        return "Tavily API key is not configured."

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
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
            title = result.get("title", "")
            url = result.get("url", "")
            content = result.get("content", "")

            results.append(
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Content:\n{content}"
            )

        if not results:
            return "No useful study material was found."

        return "\n\n---\n\n".join(results)

    except requests.RequestException as error:
        return f"Tavily search failed: {error}"

    except Exception as error:
        return f"Study search failed: {error}"
