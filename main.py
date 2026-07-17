import os
import requests

def ask_ai(text):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3.1:free",
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
summary = ask_ai(
    "در یک جمله کوتاه به فارسی بگو سلام از OpenRouter"
)

message = summary
