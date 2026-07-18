import json

HISTORY_FILE = "storage/history.json"


def load_history():

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return []


def save_history(data):

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def already_sent(title):

    history = load_history()

    return title in history


def mark_sent(title):

    history = load_history()

    history.append(title)

    history = history[-500:]

    save_history(history)
