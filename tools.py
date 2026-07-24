from ddgs import DDGS
from tavily import TavilyClient
import arxiv
import os
from dotenv import load_dotenv
import requests

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query):

    results = []

    with DDGS() as ddgs:

        for r in ddgs.text(query, max_results=5):

            results.append({
                "title": r["title"],
                "url": r["href"],
                "snippet": r["body"]
            })

    return results


def search_tavily(query):

    response = tavily_client.search(
        query=query,
        max_results=5
    )

    results = []

    for r in response["results"]:

        results.append({
            "title": r["title"],
            "url": r["url"],
            "snippet": r["content"]
        })

    return results

import arxiv


def search_arxiv(query):

    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []

    for paper in client.results(search):

        papers.append({
            "title": paper.title,
            "url": paper.entry_id,
            "snippet": paper.summary
        })

    return papers

def search_github(query):

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }

    response = requests.get(url, params=params, timeout=20)

    items = response.json().get("items", [])

    results = []

    for repo in items:

        results.append({
            "title": repo["full_name"],
            "url": repo["html_url"],
            "snippet": repo.get("description", "")
        })

    return results

def search_huggingface(query):

    url = "https://huggingface.co/api/models"

    response = requests.get(
        url,
        params={
            "search": query,
            "limit": 5
        },
        timeout=20
    )

    data = response.json()

    results = []

    for model in data:

        results.append({
            "title": model["id"],
            "url": f"https://huggingface.co/{model['id']}",
            "snippet": f"Downloads: {model.get('downloads',0)}"
        })

    return results

def search_openai_blog(query):

    return search_web(
        f"site:openai.com/news {query}"
    )

def search_google_ai(query):

    return search_web(
        f"site:blog.google/technology/ai {query}"
    )

def search_nvidia_blog(query):

    return search_web(
        f"site:developer.nvidia.com/blog {query}"
    )


# ==========================
# MEDICINE
# ==========================

def search_pubmed(query):
    return search_web(f"site:pubmed.ncbi.nlm.nih.gov {query}")

def search_clinicaltrials(query):
    return search_web(f"site:clinicaltrials.gov {query}")

def search_who(query):
    return search_web(f"site:who.int {query}")

def search_nih(query):
    return search_web(f"site:nih.gov {query}")


# ==========================
# BUSINESS
# ==========================

def search_worldbank(query):
    return search_web(f"site:worldbank.org {query}")

def search_sec(query):
    return search_web(f"site:sec.gov {query}")

def search_yahoo_finance(query):
    return search_web(f"site:finance.yahoo.com {query}")

def search_investopedia(query):
    return search_web(f"site:investopedia.com {query}")


# ==========================
# HISTORY
# ==========================

def search_wikipedia(query):
    return search_web(f"site:wikipedia.org {query}")

def search_internet_archive(query):
    return search_web(f"site:archive.org {query}")

def search_library_of_congress(query):
    return search_web(f"site:loc.gov {query}")

def search_britannica(query):
    return search_web(f"site:britannica.com {query}")


# ==========================
# SPORTS
# ==========================

def search_fifa(query):
    return search_web(f"site:fifa.com {query}")

def search_icc(query):
    return search_web(f"site:icc-cricket.com {query}")

def search_olympics(query):
    return search_web(f"site:olympics.com {query}")

def search_espn(query):
    return search_web(f"site:espn.com {query}")


# ==========================
# FASHION
# ==========================

def search_vogue(query):
    return search_web(f"site:vogue.com {query}")

def search_wwd(query):
    return search_web(f"site:wwd.com {query}")

def search_fashionunited(query):
    return search_web(f"site:fashionunited.com {query}")

def search_businessoffashion(query):
    return search_web(f"site:businessoffashion.com {query}")
