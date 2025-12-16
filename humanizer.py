from typing import Literal, Optional
import random
from openai import OpenAI

Style = Literal["friendly", "casual", "professional"]

def humanize(
    text: str,
    style: Style = "friendly",
    api_key: str | None = None,
    seed: Optional[int] = None
) -> str:
    if not api_key:
        raise RuntimeError("API key missing")

    if seed is not None:
        random.seed(seed)

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    system_prompt = (
        "You are a human editor. Rewrite text to sound natural, clear, "
        "and written by a real person. Preserve the original meaning. "
        "Avoid sounding like an assistant."
    )

    user_prompt = (
        f"Style: {style}\n\n"
        f"Text:\n{text}\n\n"
        f"Rewrite:"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=400,
    )

    return response.choices[0].message.content.strip()
