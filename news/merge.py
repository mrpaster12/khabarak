from ai.router import ask_ai
import json
import re


def merge_cluster(cluster):

    text = ""

    for item in cluster:

        text += f"""
منبع: {item['source']}

عنوان:
{item['title']}

متن:
{item['summary']}
----------------
"""

    prompt = f"""
تو سردبیر ارشد یک خبرگزاری هستی.

چند خبر مشابه از منابع مختلف دریافت کرده‌ای.

کار تو:

1- خبرها را ادغام کن.
2- اطلاعات تکراری را حذف کن.
3- فقط واقعیت‌های مشترک را نگه دار.
4- خروجی فقط JSON باشد.

فرمت:

{{
 "importance": 8,
 "title": "عنوان نهایی",
 "summary": "خلاصه نهایی",
 "sources": ["BBC","Reuters"],
 "category": "POLITICS"
}}

خبرها:

{text}
"""

    result = ask_ai(prompt)

    try:

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        return json.loads(match.group())

    except:

        return None
