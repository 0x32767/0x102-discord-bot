from pickle import load as pickle_load, dump as pickle_dump
from better_profanity import Profanity


def dump(file: str) -> None:
    profanityFilter = Profanity()
    profanityFilter.load_censor_words_from_file(
        "D:\\programing\\0x102-discord-bot\\assets\\profanity.json"
    )

    with open(file, "wb") as f:
        pickle_dump(profanityFilter, f)


def load(file: str) -> Profanity:
    try:
        with open(file, "rb") as f:
            return pickle_load(f)

    except FileNotFoundError:
        return None


def check_raw(text: str) -> bool:
    profanityFilter: Profanity = load(
        "D:\\programing\\0x102-discord-bot\\assets\\profanity.pkl"
    )

    return profanityFilter.censor_text(text)
