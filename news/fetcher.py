import feedparser
from news.rss_sources import RSS_FEEDS

def fetch_news():

    news = []

    for url in RSS_FEEDS:

        try:

            feed = feedparser.parse(url)

            source = feed.feed.get("title", url)

            for entry in feed.entries[:20]:

                news.append({
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "link": entry.get("link", ""),
                    "source": source,
                })

        except Exception as e:

            print(f"ERROR {url}: {e}")

    return news
