import os
import requests

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/auto",
        "max_tokens": 150,
        "messages": [
            {
                "role": "user",
                "content": "در یک جمله کوتاه به فارسی بگو سلام"
            }
        ]
    }
)

print(response.status_code)
print(response.text)
