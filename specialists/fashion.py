from specialists.base_specialist import run_specialist
from sources.fashion_sources import FASHION_SOURCES

def fashion_specialist(query):
    return run_specialist(
        query=query,
        domain="Fashion",
        sources=FASHION_SOURCES
    )