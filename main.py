from news.fetcher import fetch_news
from news.deduplicate import remove_duplicates
from news.history import already_sent
from news.history import mark_sent

from news.summarize import summarize_news
from news.summarize import parse_ai_result

from publishers.telegram import send_message


def build_message(data):

    return f"""
🚨 {data['title']}

📊 اهمیت: {data['importance']}/10

📰 خلاصه:

{data['summary']}

🏷 دسته:
{data['category']}
""".strip()


def main():

    news = fetch_news()

    news = remove_duplicates(news)

    print(f"News Count: {len(news)}")

    candidates = []

    for item in news[:30]:

        if already_sent(item["title"]):
            continue

        try:

            result = summarize_news(
                item["title"],
                item["summary"]
            )

            parsed = parse_ai_result(
                result
            )

            if not parsed:
                continue

            importance = int(
                parsed["importance"]
            )

            if importance < 5:
                continue

            candidates.append(
                (
                    importance,
                    parsed,
                    item["title"]
                )
            )

        except Exception as e:

            print(e)

    if not candidates:

        print("No Important News")
        return

    candidates.sort(
        key=lambda x: x[0],
        reverse=True
    )

    best = candidates[0]

    message = build_message(
        best[1]
    )

    send_message(message)

    mark_sent(
        best[2]
    )

    print("News Sent")


if __name__ == "__main__":
    main()
