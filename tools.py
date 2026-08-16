from ddgs import DDGS
from tavily import TavilyClient

import os
from dotenv import load_dotenv
import requests

load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# ============================================================
# GENERAL WEB SEARCH
# ============================================================

def search_web(query):

    results = []

    try:

        with DDGS() as ddgs:

            for r in ddgs.text(
                query,
                max_results=5
            ):

                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", "")
                })

    except Exception as e:

        print("search_web error:", e)

    return results


# ============================================================
# TAVILY
# ============================================================

def search_tavily(query):

    results = []

    try:

        response = tavily_client.search(
            query=query,
            max_results=5
        )

        for r in response.get("results", []):

            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "snippet": r.get("content", "")
            })

    except Exception as e:

        print("search_tavily error:", e)

    return results




# ============================================================
# GITHUB
# ============================================================

def search_github(query):

    results = []

    try:

        url = "https://api.github.com/search/repositories"

        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 5
        }

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        items = response.json().get(
            "items",
            []
        )

        for repo in items:

            results.append({
                "title": repo["full_name"],
                "url": repo["html_url"],
                "snippet": repo.get(
                    "description",
                    ""
                )
            })

    except Exception as e:

        print("search_github error:", e)

    return results


# ============================================================
# HUGGING FACE
# ============================================================

def search_huggingface(query):

    results = []

    try:

        url = "https://huggingface.co/api/models"

        response = requests.get(
            url,
            params={
                "search": query,
                "limit": 5
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        for model in data:

            model_id = model.get(
                "id",
                ""
            )

            results.append({
                "title": model_id,
                "url": f"https://huggingface.co/{model_id}",
                "snippet": (
                    f"Downloads: "
                    f"{model.get('downloads', 0)}"
                )
            })

    except Exception as e:

        print("search_huggingface error:", e)

    return results


# ============================================================
# TECHNOLOGY SPECIALIZED SOURCES
# ============================================================

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


# ============================================================
# MEDICINE — PUBMED
# ============================================================

def search_pubmed(query):

    results = []

    try:

        url = (
            "https://eutils.ncbi.nlm.nih.gov/"
            "entrez/eutils/esearch.fcgi"
        )

        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 5
        }

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        ids = response.json() \
            .get("esearchresult", {}) \
            .get("idlist", [])

        if not ids:
            return results

        summary_url = (
            "https://eutils.ncbi.nlm.nih.gov/"
            "entrez/eutils/esummary.fcgi"
        )

        summary_response = requests.get(
            summary_url,
            params={
                "db": "pubmed",
                "id": ",".join(ids),
                "retmode": "json"
            },
            timeout=20
        )

        summary_response.raise_for_status()

        data = summary_response.json()

        for pubmed_id in ids:

            article = data.get(
                "result",
                {}
            ).get(
                pubmed_id,
                {}
            )

            results.append({
                "title": article.get(
                    "title",
                    ""
                ),
                "url": (
                    "https://pubmed.ncbi.nlm.nih.gov/"
                    f"{pubmed_id}/"
                ),
                "snippet": (
                    f"PubMed article. "
                    f"Published: "
                    f"{article.get('pubdate', '')}"
                )
            })

    except Exception as e:

        print("search_pubmed error:", e)

    return results


# ============================================================
# MEDICINE — CLINICALTRIALS.GOV
# ============================================================

def search_clinicaltrials(query):

    results = []

    try:

        url = (
            "https://clinicaltrials.gov/"
            "api/v2/studies"
        )

        response = requests.get(
            url,
            params={
                "query.term": query,
                "pageSize": 5,
                "format": "json"
            },
            timeout=20
        )

        response.raise_for_status()

        studies = response.json().get(
            "studies",
            []
        )

        for study in studies:

            protocol = study.get(
                "protocolSection",
                {}
            )

            identification = protocol.get(
                "identificationModule",
                {}
            )

            description = protocol.get(
                "descriptionModule",
                {}
            )

            study_id = identification.get(
                "nctId",
                ""
            )

            title = identification.get(
                "briefTitle",
                ""
            )

            results.append({
                "title": title,
                "url": (
                    "https://clinicaltrials.gov/"
                    f"study/{study_id}"
                ),
                "snippet": description.get(
                    "briefSummary",
                    ""
                )
            })

    except Exception as e:

        print(
            "search_clinicaltrials error:",
            e
        )

    return results


# ============================================================
# MEDICINE — WHO
# ============================================================

def search_who(query):

    return search_web(
        f"site:who.int {query}"
    )


# ============================================================
# MEDICINE — NIH
# ============================================================

def search_nih(query):

    return search_web(
        f"site:nih.gov {query}"
    )

# ============================================================
# FALLBACK FOR ADDITIONAL DOMAIN SOURCES
# ============================================================

def __getattr__(name):

    if name.startswith("search_"):

        def generic_search(query):

            return search_web(query)

        return generic_search

    raise AttributeError(
        f"module 'tools' has no attribute '{name}'"
    )