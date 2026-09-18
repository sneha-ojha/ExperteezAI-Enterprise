from specialists.base_specialist import run_specialist

from sources.medicine_sources import MEDICINE_SOURCES


def medicine_specialist(
    query,
    output_type,
    output_length,
    public_sources
):
    return run_specialist(
        query=query,
        domain="Medicine",
        sources=MEDICINE_SOURCES,
        output_type=output_type,
        output_length=output_length,
        public_sources=public_sources
    )