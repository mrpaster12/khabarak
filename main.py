from news.fetcher import fetch_news
from news.deduplicate import remove_duplicates
from news.summarize import summarize_news

from publishers.telegram import send_message

news = fetch_news()

news = remove_duplicates(news)

print(f"Total News: {len(news)}")

processed = 0

for item in news[:20]:

    try:

        result = summarize_news(
            item["title"],
            item["summary"]
        )

        print(result)

        if "SKIP" in result:
            continue

        send_message(
            f"📰 {result}"
        )

        processed += 1

        if processed >= 5:
            break

    except Exception as e:

        print(e)
