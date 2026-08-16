from router import route


def run_agent(domain, query):

    specialist = route(domain)

    if specialist is None:

        raise ValueError(f"Unknown research domain: {domain}")

    result = specialist(query)

    return {
        "plan": result["plan"],
        "evidence": result["evidence"],
        "reflection": result["reflection"]
    }