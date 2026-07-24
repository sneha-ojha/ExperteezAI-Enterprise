from ddgs import DDGS
from tavily import TavilyClient
import arxiv
import os
from dotenv import load_dotenv

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