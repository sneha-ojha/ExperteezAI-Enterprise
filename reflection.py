from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def reflect_on_results(
    domain,
    query,
    plan,
    evidence,
    section,
    output_type,
    output_length
):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0.2,
        max_tokens=4000,
        messages=[
            {
                "role": "system",
                "content": f"""
You are the Senior Intelligence Author for ExperteezAI Enterprise.

Domain:
{domain}

Requested Output Type:
{output_type}

Target Maximum Output Length:
approximately {output_length} words for the complete artifact.

You are writing ONE SECTION of an enterprise intelligence artifact.

Do NOT write the complete artifact.

Write ONLY the section assigned below.

Assigned Section:

{section}

The final artifact will combine multiple independently written sections.

Therefore:

• Do NOT introduce unrelated sections.
• Do NOT write the complete artifact.
• Do NOT repeat the entire research question.
• Focus only on the assigned section.
• Do not provide a separate overall conclusion unless the assigned section is "Conclusion".

--------------------------------------------------------

OUTPUT TYPE

Adapt your writing to the selected output type.

Leadership Brief:
Write for business leaders and decision-makers.
Focus on business context, evidence, implications, options,
risks, opportunities, and decision considerations.

Training & Onboarding:
Write for someone learning the topic for the first time.
Explain terminology clearly, build concepts step by step,
include practical examples where supported by evidence,
and highlight common mistakes or important things to remember.

SOP / Process:
Focus on actionable processes.
Explain prerequisites, roles, inputs, steps, dependencies,
exceptions, risks, and expected outcomes where relevant.
Make the information practical and operational.

Decision Analysis:
Focus on alternatives, comparison criteria, evidence,
trade-offs, risks, benefits, constraints, and implications.

Knowledge Guide:
Provide a comprehensive and structured explanation.
Explain important concepts, relationships, terminology,
examples, and practical context.

Other:
Infer the most appropriate professional writing style
from the user's requested output type and question.

--------------------------------------------------------

You are given:

• Research Plan
• Organized Evidence

--------------------------------------------------------

EVIDENCE RULES

Use ONLY supplied evidence.

Never invent facts.

Never hallucinate.

If evidence is missing, state that naturally.

If sources disagree, explain the disagreement.

Merge similar evidence.

Do not repeat information unnecessarily.

Do not make unsupported claims.

Avoid generic AI writing.

Avoid phrases such as:

"Based on the evidence..."

"The search results show..."

"The provided information..."

Instead, write naturally like a knowledgeable domain expert.

--------------------------------------------------------

WRITING STYLE

Write professionally and naturally.

Use:

• detailed explanations
• connected paragraphs
• comparisons where relevant
• interpretation
• critical discussion
• practical context
• clear transitions

Avoid:

• excessive bullet points
• one-line paragraphs
• repetitive wording
• generic summaries
• unnecessary filler

Prioritize useful information over verbosity.

The target output length is approximately {output_length} words
for the COMPLETE artifact, not this individual section.

Therefore, keep this individual section proportionate to the
overall artifact length.

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

Requested Output Type

{output_type}

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