from tools import search_web, search_tavily


def execute_research(query):

    results = {}

    try:
        print("Searching DDGS...")
        results["ddgs"] = search_web(query)
        print("DDGS Done")
    except Exception as e:
        print("DDGS Error:", e)
        results["ddgs"] = []

    try:
        print("Searching Tavily...")
        results["tavily"] = search_tavily(query)
        print("Tavily Done")
    except Exception as e:
        print("Tavily Error:", e)
        results["tavily"] = []

    # Temporarily disable arXiv
    results["arxiv"] = []

    return results