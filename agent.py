from router import route


def run_agent(domain, query):

    specialist = route(domain)

    if specialist is None:
        return "Unknown domain."

    return specialist(query)