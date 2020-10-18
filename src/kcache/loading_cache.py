from kcache.basecache import BaseCache
from kcache.cacheloader import CacheLoader


class LoadingCache(BaseCache):

    def size(self):
        return len(self._dict)

    # def stats(self):
    #     pass

    def cleanup(self):
        if self._loader:
            self._loader.close()

    def __init__(self, loader: CacheLoader, initial_cache: dict = None) -> None:
        if initial_cache:
            self._dict: initial_cache
        else:
            self._dict = dict()
        self._loader: CacheLoader = loader

    def get_all_present(self, keys) -> dict:
        r = {}
        for key in keys:
            value = self.get_if_present(key=key)
            if value:
                r[key] = value
        return r

    def get_if_present(self, key):
        if key in self._dict:
            return self._dict[key]
        return None

    def put_all(self, d: dict):
        if not d:
            return
        for k, v in d.items():
            self.put(key=k, value=v)

    def put(self, key, value):
        if key in self._dict:
            # TODO call listener
            pass
        self._dict[key] = value

    def invalidate_all(self, keys):
        for k in keys:
            self.invalidate(key=k)

    def invalidate_all_elements(self):
        for k in self._dict:
            self.invalidate(key=k)

    def invalidate(self, key):
        if key in self._dict:
            # TODO call listener
            del self._dict[key]

    def get(self, key):
        if key in self._dict:
            return self._dict[key]
        elif self._loader:
            value = self._loader.load(key)
            self.put(key=key, value=value)
            return value

    def as_dict(self):
        return self._dict.copy()
