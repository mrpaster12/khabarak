from news.fetcher import fetch_news
from news.deduplicate import remove_duplicates

news = fetch_news()

print(f"Fetched: {len(news)}")

news = remove_duplicates(news)

print(f"Unique: {len(news)}")

for item in news[:10]:

    print("=" * 50)
    print(item["title"])
    print(item["source"])
