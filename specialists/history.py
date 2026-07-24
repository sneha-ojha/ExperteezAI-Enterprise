from specialists.base_specialist import run_specialist
from sources.history_sources import HISTORY_SOURCES

def history_specialist(query):
    return run_specialist(
        query=query,
        domain="History",
        sources=HISTORY_SOURCES
    )