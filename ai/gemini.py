from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY_1")
)

def summarize_news(title, summary):

    prompt = f"""
تو یک سردبیر خبری حرفه‌ای هستی.

خبر زیر را بررسی کن.

عنوان:
{title}

متن:
{summary}

اگر خبر مهم نیست فقط بنویس:

SKIP

اگر مهم است خروجی را به این شکل بده:

اهمیت: X/10

خلاصه:
(حداکثر ۳ جمله فارسی)
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
