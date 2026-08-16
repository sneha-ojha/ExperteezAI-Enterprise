from tools import (
    search_web,
    search_tavily,
    search_github,
    search_huggingface,
    search_openai_blog,
    search_google_ai,
    search_nvidia_blog,
)

TECHNOLOGY_SOURCES = [
    search_github,
    search_huggingface,
    search_openai_blog,
    search_google_ai,
    search_nvidia_blog,
    search_tavily,
    search_web,
]