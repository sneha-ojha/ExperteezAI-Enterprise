from specialists.base_specialist import run_specialist

from sources.fashion_sources import FASHION_SOURCES


def fashion_specialist(
    query,
    output_type,
    output_length,
    public_sources
):
    return run_specialist(
        query=query,
        domain="Fashion",
        sources=FASHION_SOURCES,
        output_type=output_type,
        output_length=output_length,
        public_sources=public_sources
    )