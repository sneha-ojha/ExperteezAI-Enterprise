from router import route


def run_agent(
    domain,
    query,
    output_type,
    output_length,
    public_sources
):

    specialist = route(domain)

    if specialist is None:
        raise ValueError(f"Unknown domain: {domain}")

    # Generic specialist needs the selected domain.
    if specialist.__name__ == "generic_specialist":
        events = specialist(
            query=query,
            domain=domain,
            output_type=output_type,
            output_length=output_length,
            public_sources=public_sources
        )
    else:
        events = specialist(
            query=query,
            output_type=output_type,
            output_length=output_length,
            public_sources=public_sources
        )

    for event in events:
        yield event