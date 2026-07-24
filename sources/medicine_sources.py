from tools import (
    search_web,
    search_tavily,
    search_pubmed,
    search_clinicaltrials,
    search_who,
    search_nih,
)

MEDICINE_SOURCES = [
    search_pubmed,
    search_clinicaltrials,
    search_who,
    search_nih,
    search_tavily,
    search_web,
]