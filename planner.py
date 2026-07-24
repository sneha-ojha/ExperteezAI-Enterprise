from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def create_research_plan(domain, query):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert research planner.

Domain:
{domain}

Your job is NOT to answer the question.

Instead create a research plan.

Return the plan using exactly this format:

Goal:
...

Information Needed:
- ...
- ...

Suggested Sources:
- ...

Suggested Tools:
- ...

Research Strategy:
...
"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content