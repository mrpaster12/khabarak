from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY_1")
)

PROMPT = """
تو یک سردبیر خبری حرفه‌ای هستی.

قوانین:

1- فقط خبرهای مهم و نیمه مهم را منتشر کن.
2- خبرهای محلی، تبلیغاتی، ورزشی عادی و کم اهمیت را رد کن.
3- اگر خبر مهم نیست فقط بنویس:

SKIP

4- اگر خبر مهم است خروجی دقیقاً به این شکل باشد:

IMPORTANCE: عدد بین 1 تا 10

SUMMARY:
خلاصه فارسی در حداکثر 3 جمله
"""

def summarize_news(title, summary):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{PROMPT}

عنوان:
{title}

متن:
{summary}
"""
    )

    return response.text
