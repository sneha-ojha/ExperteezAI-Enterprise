from specialists.base_specialist import run_specialist
from sources.business_sources import BUSINESS_SOURCES

def business_specialist(query):
    return run_specialist(
        query=query,
        domain="Business",
        sources=BUSINESS_SOURCES
    )