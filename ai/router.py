import os

from ai.gemini import ask_gemini
from ai.groq import ask_groq


def ask_ai(prompt):

    keys = [
        os.getenv("GEMINI_API_KEY_1"),
        os.getenv("GEMINI_API_KEY_2"),
        os.getenv("GEMINI_API_KEY_3")
    ]

    for key in keys:

        if not key:
            continue

        try:

            print("Using Gemini")

            return ask_gemini(
                key,
                prompt
            )

        except Exception as e:

            print(e)

    print("Using Groq")

    return ask_groq(prompt)
