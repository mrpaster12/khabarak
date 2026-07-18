import os

from google import genai

from ai.groq import ask_groq


def ask_gemini(api_key, prompt):

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def ask_ai(prompt):

    gemini_keys = [
        os.getenv("GEMINI_API_KEY_1"),
        os.getenv("GEMINI_API_KEY_2"),
        os.getenv("GEMINI_API_KEY_3")
    ]

    for key in gemini_keys:

        if not key:
            continue

        try:
            print("Using Gemini")

            return ask_gemini(
                key,
                prompt
            )

        except Exception as e:

            print(f"Gemini Failed: {e}")

    print("Using Groq")

    return ask_groq(prompt)
