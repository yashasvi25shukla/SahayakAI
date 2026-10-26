import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing from .env file."
    )

client = genai.Client(api_key=API_KEY)

PRIMARY_MODEL = "gemini-3.5-flash-lite"
FALLBACK_MODEL = "gemini-3.8-flash"


def build_prompt(question: str) -> str:

    return f"""
You are SahayakAI, a fast AI assistant for
Indian government schemes.

Answer in very simple English, Hindi, or Hinglish.

Rules:
- Keep answer short.
- Maximum 4 bullet points.
- No long explanation.
- Explain benefits and eligibility simply.
- Do not invent government rules.
- Do not invent deadlines or links.
- If asked about a current deadline, say:
  "Please verify the latest deadline on the official
  government portal because deadlines may change."
- Mention official verification briefly.

Question:
{question}
"""


def call_model(model_name: str, prompt: str):

    thinking_level = (
        "minimal"
        if model_name == "gemini-3.5-flash-lite"
        else "low"
    )

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level=thinking_level
            ),
            max_output_tokens=180
        )
    )

    if not response.text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return response.text


def ask_gemini(question: str):

    if not question or not question.strip():
        raise ValueError(
            "Question cannot be empty."
        )

    prompt = build_prompt(question)

    models = [
        PRIMARY_MODEL,
        FALLBACK_MODEL
    ]

    last_error = None

    for model_name in models:

        try:

            print(
                f"Calling Gemini: {model_name}"
            )

            answer = call_model(
                model_name,
                prompt
            )

            print(
                f"Gemini success: {model_name}"
            )

            return answer

        except Exception as error:

            last_error = error

            print(
                f"Gemini error on {model_name}:",
                error
            )

            error_text = str(error).lower()

            temporary_error = any(
                text in error_text
                for text in [
                    "503",
                    "high demand",
                    "service unavailable",
                    "429",
                    "resource exhausted",
                    "timeout"
                ]
            )

            # Only one very short retry
            if temporary_error:

                time.sleep(0.5)

                try:

                    return call_model(
                        model_name,
                        prompt
                    )

                except Exception as retry_error:

                    last_error = retry_error

            # Immediately move to fallback
            continue

    raise RuntimeError(
        "SahayakAI is temporarily busy. "
        "Please try again. "
        f"Last error: {last_error}"
    )