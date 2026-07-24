from specialists.base_specialist import run_specialist
from sources.medicine_sources import MEDICINE_SOURCES

def medicine_specialist(query):
    return run_specialist(
        query=query,
        domain="Medicine",
        sources=MEDICINE_SOURCES
    )