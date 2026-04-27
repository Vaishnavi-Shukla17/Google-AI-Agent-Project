import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 5):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            return results if results else []
    except Exception:
        return []

def scrape_content(url: str, max_chars: int = 3000) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        return " ".join(text.split())[:max_chars]
    except Exception:
        return ""

def collect_research_context(query: str, max_results: int = 5) -> str:
    results = search_web(query, max_results=max_results)

    if not results:
        return "No research sources found for this query."

    collected = []
    for i, result in enumerate(results, start=1):
        title = result.get("title", "No title")
        url = result.get("href", "")
        snippet = result.get("body", "")

        page_text = scrape_content(url) if url else ""

        collected.append(
            f"Source {i}\n"
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Snippet: {snippet}\n"
            f"Content: {page_text}\n"
        )

    return "\n\n".join(collected)
