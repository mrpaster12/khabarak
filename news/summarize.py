import json
import re

from ai.router import ask_ai


PROMPT = """
تو یک سردبیر حرفه‌ای خبر هستی.

خبر را بررسی کن.

اگر خبر بی اهمیت است فقط بنویس:

SKIP

اگر خبر مهم است فقط JSON برگردان.

فرمت:

{
  "importance": 8,
  "title": "عنوان کوتاه فارسی",
  "summary": "حداکثر 3 جمله",
  "category": "POLITICS"
}

فقط JSON برگردان.
"""


def summarize_news(title, summary):

    prompt = f"""
{PROMPT}

عنوان:
{title}

متن:
{summary}
"""

    return ask_ai(prompt)


def parse_ai_result(text):

    if "SKIP" in text.upper():
        return None

    try:

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if not match:
            return None

        return json.loads(
            match.group()
        )

    except Exception:
        return None
