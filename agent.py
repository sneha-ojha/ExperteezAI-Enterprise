from router import route


def run_agent(domain, query):

    specialist = route(domain)

    if specialist is None:
        raise ValueError(f"Unknown research domain: {domain}")

    for event in specialist(query):

        yield event