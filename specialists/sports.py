from specialists.base_specialist import run_specialist
from sources.sports_sources import SPORTS_SOURCES

def sports_specialist(query):
    return run_specialist(
        query=query,
        domain="Sports",
        sources=SPORTS_SOURCES
    )