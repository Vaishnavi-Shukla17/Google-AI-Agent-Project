from duckduckgo_search import DDGS

print("🧪 Testing DuckDuckGo Search...")
try:
    with DDGS() as ddgs:
        results = [r for r in ddgs.text("climate change crop yields", max_results=3)]
    print(f"✅ FOUND {len(results)} results:")
    for r in results:
        print(f"- {r['title']}")
except Exception as e:
    print(f"❌ SEARCH ERROR: {e}")
