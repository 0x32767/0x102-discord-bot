"""
 | The poinmt of the cache is the to keep track of all the data in one place.
 | This dataincludes the guild id which is stored in the `constants.conf` file
 | but is accessed only once and is then stored min the cache.
"""

cache = {}

def cacheGet(key: str) -> any:
    """
    :param key: The `key` is the key of the cache
    :return:
    """
    return cache[key]


def cacheSet(key: str, value: any) -> None:
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
