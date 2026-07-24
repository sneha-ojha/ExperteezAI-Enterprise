from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def synthesize_evidence(domain, query, plan, search_results):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert research evidence synthesizer.

Domain:
{domain}

You are given:

• A research plan
• Search results from multiple search engines

Your job is NOT to answer the research question.

Your job is to organize the evidence.

Instructions:

1. Group similar findings together.
2. Remove duplicate information.
3. Identify agreements between sources.
4. Identify conflicting information.
5. Ignore advertisements.
6. Ignore low-quality results.
7. Mention missing information.
8. Preserve important technical details.

Return this structure exactly:

# Organized Evidence

## Topic 1
Evidence
Sources
Confidence

## Topic 2
Evidence
Sources
Confidence

## Conflicting Information

## Missing Information
"""
            },
            {
                "role": "user",
                "content": f"""
Research Query

{query}

Research Plan

{plan}

Search Results

{json.dumps(search_results, indent=2)}
"""
            }
        ]
    )

    return response.choices[0].message.content