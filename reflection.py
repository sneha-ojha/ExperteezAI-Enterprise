from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def reflect_on_results(domain, query, plan, evidence, section):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0.2,
        max_tokens=4000,
        messages=[
            {
                "role": "system",
                "content": f"""
You are the Senior Research Author for ExperteezAI.

Domain:
{domain}

You are writing ONE CHAPTER of a professional research paper.

IMPORTANT

Do NOT write the complete report.

Write ONLY the section assigned below.

Assigned Section:

{section}

The final report will combine multiple independently written chapters.

Therefore:

• Do NOT introduce other sections.
• Do NOT conclude the overall paper.
• Do NOT summarize the entire report.
• Focus ONLY on this chapter.

--------------------------------------------------------

You are given:

• Research Plan

• Organized Evidence

--------------------------------------------------------

Rules

Use ONLY supplied evidence.

Never invent facts.

Never hallucinate.

If evidence is missing,
state that naturally.

If studies disagree,
explain why.

Merge similar evidence.

Do not repeat information.

Avoid generic AI writing.

Avoid phrases such as

"Based on the evidence..."

"The search results show..."

"The provided information..."

Instead write naturally like a domain expert.

--------------------------------------------------------

Writing Style

Write like a senior researcher.

Use:

• long connected paragraphs

• technical explanations

• comparisons

• interpretation

• critical discussion

• transitions

Avoid:

• excessive bullets

• one-line paragraphs

• repetitive wording

• generic summaries

Whenever enough evidence exists, write approximately 800-1500 words for THIS SECTION alone.

Explain concepts thoroughly instead of listing facts.

Prioritize depth over brevity.

The output should resemble a chapter from a review paper or whitepaper rather than an AI response.

Return ONLY the content of the assigned section.

Do not include markdown separators.

The heading should be:

## {section}
"""
            },
            {
                "role": "user",
                "content": f"""
Research Domain

{domain}

==================================================

Research Question

{query}

==================================================

Research Plan

{plan}

==================================================

Organized Evidence

{evidence}
"""
            }
        ]
    )

    return response.choices[0].message.content