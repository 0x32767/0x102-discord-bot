"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
