from specialists.base_specialist import run_specialist

from sources.technology_sources import TECHNOLOGY_SOURCES


def technology_specialist(query):

    return run_specialist(

        query=query,

        domain="Technology",

        sources=TECHNOLOGY_SOURCES
    )