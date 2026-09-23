"""System 1: plain chatbot. It does not receive the private fee data."""

from config import client, MODEL, QUESTIONS, banner

SYSTEM_PROMPT = """You are a helpful college assistant.
Answer the user's questions clearly and concisely.
If you do not know a fact, say you do not know.
"""

banner("SYSTEM 1 — PLAIN CHATBOT")

for q in QUESTIONS:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
        ],
        temperature=0,
    )

    print(f"Q: {q}")
    print(f"A: {response.choices[0].message.content.strip()}\n")