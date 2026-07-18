from news.fetcher import fetch_news
from news.deduplicate import remove_duplicates
from news.cluster import cluster_news
from news.merge import merge_cluster

from news.history import already_sent
from news.history import mark_sent

from publishers.telegram import send_message


def build_message(data):

    sources = " | ".join(
        data.get("sources", [])
    )

    return f"""
🚨 {data['title']}

📊 اهمیت: {data['importance']}/10

📰 خلاصه:

{data['summary']}

📚 منابع:
{sources}

🏷 دسته:
{data['category']}
""".strip()


def main():

    news = fetch_news()

    news = remove_duplicates(news)

    print(f"Fetched {len(news)}")

    clusters = cluster_news(news)

    print(f"Clusters {len(clusters)}")

    candidates = []

    for cluster in clusters:

        title = cluster[0]["title"]

        if already_sent(title):
            continue

        try:

            merged = merge_cluster(
                cluster
            )

            if not merged:
                continue

            importance = int(
                merged["importance"]
            )

            if importance < 6:
                continue

            candidates.append(
                (
                    importance,
                    merged,
                    title
                )
            )

        except Exception as e:

            print(e)

    if not candidates:
        print("No news")
        return

    candidates.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    best = candidates[0]

    send_message(
        build_message(
            best[1]
        )
    )

    mark_sent(
        best[2]
    )

    print("Sent")
    

if __name__ == "__main__":
    main()
