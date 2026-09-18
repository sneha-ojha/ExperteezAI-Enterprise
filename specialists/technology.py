from specialists.base_specialist import run_specialist

from sources.technology_sources import TECHNOLOGY_SOURCES


def technology_specialist(
    query,
    output_type,
    output_length,
    public_sources
):
    return run_specialist(
        query=query,
        domain="Technology",
        sources=TECHNOLOGY_SOURCES,
        output_type=output_type,
        output_length=output_length,
        public_sources=public_sources
    )