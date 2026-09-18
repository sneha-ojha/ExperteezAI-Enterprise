from specialists.base_specialist import run_specialist


def generic_specialist(
    query,
    domain,
    output_type,
    output_length,
    public_sources
):
    return run_specialist(
        query=query,
        domain=domain,
        sources=[],
        output_type=output_type,
        output_length=output_length,
        public_sources=public_sources
    )