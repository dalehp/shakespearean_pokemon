from typing import Optional


CACHE = None


class DescriptionCache:
    """ In memory cache for pokemon descriptions.

    Consider replacing with more persistent storage"""

    def __init__(self):
        self._cache = {}

    def save(self, name: str, description: str):
        self._cache[name] = description

    def get(self, name: str) -> Optional[str]:
        return self._cache.get(name)


def get_cache():
    global CACHE
    if CACHE is None:
        CACHE = DescriptionCache()
    return CACHE
