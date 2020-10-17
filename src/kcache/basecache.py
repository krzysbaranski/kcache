from abc import abstractmethod

from kcache.cache import Cache


class BaseCache(Cache):

    @abstractmethod
    def get_all_present(self, keys) -> dict:
        result = {}
        for key in keys:
            value = self.get_if_present(key=key)
            if value:
                result[key] = value
        return result

    @abstractmethod
    def put_all(self, d: dict):
        if not d:
            return
        for key, value in d.items():
            self.put(key=key, value=value)

    @abstractmethod
    def invalidate_all(self, keys):
        if not keys:
            return
        for key in keys:
            self.invalidate(key)

