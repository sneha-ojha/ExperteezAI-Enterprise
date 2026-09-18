from concurrent.futures import ThreadPoolExecutor, as_completed


def run_tool(tool, query):

    try:
        print(f"Searching {tool.__name__}...")

        result = tool(query)

        return tool.__name__, result

    except Exception as e:

        print(tool.__name__, e)

        return tool.__name__, []


def execute_research(query, sources):

    results = {}

    if not sources:
        return results

    # Run source searches concurrently.
    max_workers = min(len(sources), 5)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        futures = [
            executor.submit(run_tool, tool, query)
            for tool in sources
        ]

        for future in as_completed(futures):

            tool_name, result = future.result()

            results[tool_name] = result

    return results