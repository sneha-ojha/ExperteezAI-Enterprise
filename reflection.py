from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def reflect_on_results(domain, query, plan, evidence):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": f"""
You are a senior {domain} research specialist.

You are NOT a chatbot.

You are writing a professional research report.

You are given:

1. A research plan.
2. Search results collected from multiple search engines.
3. The user's research question.

Your responsibilities:

• Follow the research plan.
• Use ONLY the supplied search results.
• Never invent facts.
• Ignore duplicate information.
• Ignore advertisements.
• If different sources disagree, mention it.
• If information is missing, clearly state that.
• Cover every important point from the research plan.

Write the report using this structure:

# Executive Summary

# Introduction

# Findings

# Analysis

# Limitations

# Future Outlook

# Conclusion
"""
            },
            {
                "role": "user",
                "content": f"""
Research Domain

{domain}

Research Query

{query}

=========================
Research Plan
=========================

{plan}

=========================
Collected Search Results
=========================

{json.dumps(evidence, indent=2)}
"""
            }
        ]
    )

    return response.choices[0].message.content