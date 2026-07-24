def execute_research(query, sources):

    results = {}

    for tool in sources:

        try:
            print(f"Searching {tool.__name__}...")

            results[tool.__name__] = tool(query)

        except Exception as e:

            print(tool.__name__, e)

            results[tool.__name__] = []

    return results