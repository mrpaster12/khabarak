from news.fetcher import fetch_news
from news.deduplicate import remove_duplicates

from ai.gemini import summarize_news

news = fetch_news()

news = remove_duplicates(news)

print(f"Total News: {len(news)}")

first_news = news[0]

result = summarize_news(
    first_news["title"],
    first_news["summary"]
)

print(result)
