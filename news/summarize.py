from router import ask_ai


PROMPT = """
تو یک سردبیر حرفه‌ای خبر هستی.

وظایف:

1- خبر را بررسی کن.

2- اگر مهم نیست فقط بنویس:

SKIP

3- اگر مهم است خروجی دقیقا به این شکل باشد:

IMPORTANCE: عدد بین 1 تا 10

TITLE:
تیتر کوتاه فارسی

SUMMARY:
حداکثر 3 جمله فارسی

CATEGORY:
POLITICS
ECONOMY
WAR
TECH
WORLD
"""

def summarize_news(title, summary):

    prompt = f"""
{PROMPT}

TITLE:
{title}

TEXT:
{summary}
"""

    return ask_ai(prompt)
