def normalize_title(title):

    return (
        title.lower()
        .replace("،", "")
        .replace(":", "")
        .replace("-", "")
        .replace(";", "")
        .strip()
    )


def similarity(a, b):

    words_a = set(normalize_title(a).split())
    words_b = set(normalize_title(b).split())

    if not words_a or not words_b:
        return 0

    return len(words_a & words_b) / len(words_a | words_b)


def cluster_news(news, threshold=0.4):

    clusters = []

    for item in news:

        found = False

        for cluster in clusters:

            score = similarity(
                item["title"],
                cluster[0]["title"]
            )

            if score >= threshold:

                cluster.append(item)
                found = True
                break

        if not found:
            clusters.append([item])

    return clusters
