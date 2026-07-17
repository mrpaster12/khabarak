def remove_duplicates(news):

    seen = set()
    unique = []

    for item in news:

        title = item["title"].strip().lower()

        if title in seen:
            continue

        seen.add(title)
        unique.append(item)

    return unique
