from tools import (
    search_web,
    search_tavily,
    search_wikipedia,
    search_internet_archive,
    search_library_of_congress,
    search_britannica,
)

HISTORY_SOURCES = [
    search_library_of_congress,
    search_internet_archive,
    search_britannica,
    search_wikipedia,
    search_tavily,
    search_web,
]