import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    api_key = st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

AVAILABLE_DOMAINS = [
    "Technology",
    "Medicine",
    "Business",
    "History",
    "Sports",
    "Fashion"
]


def validate_domain(query):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"""
You are a domain classifier.

Your job is ONLY to classify the user's query.

Available domains:

{", ".join(AVAILABLE_DOMAINS)}

Rules:
- Return exactly ONE domain.
- Do not explain.
- Do not add punctuation.
- Never return anything except one of the domains.
"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content.strip()