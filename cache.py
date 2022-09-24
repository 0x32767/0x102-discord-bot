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
"""
 | The poinmt of the cache is the to keep track of all the data in one place.
 | This dataincludes the guild id which is stored in the `constants.conf` file
 | but is accessed only once and is then stored min the cache.
"""
from typing import TypeVar, Any


cache: dict[str, Any] = {}


def cacheGet(key: str) -> Any:
    """
    :param key: The `key` is the key of the cache
    :return:
    """
    return cache[key]


def cacheSet(key: str, value: Any) -> None:
    """
    :param key: The `key` is the key of the cache
    :param value: The `value` is the value of the cache
    :return:
    """
    cache[key] = value


def cacheFree(key: str) -> None:
    """
    :param key: The `key` is the key of the cache
    :return:
    """
    del cache[key]


def cacheClear() -> None:
    """
    :return:
    """
    cache.clear()


def cacheExist(key: str) -> bool:
    """
    :param key: The `key` is the key of the cache
    :return:
    """
    return key in cache
