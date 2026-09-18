from specialists.base_specialist import run_specialist

from sources.business_sources import BUSINESS_SOURCES


def business_specialist(
    query,
    output_type,
    output_length,
    public_sources
):
    return run_specialist(
        query=query,
        domain="Business",
        sources=BUSINESS_SOURCES,
        output_type=output_type,
        output_length=output_length,
        public_sources=public_sources
    )