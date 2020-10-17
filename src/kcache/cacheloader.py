from abc import ABC, abstractmethod
from collections.abc import Iterable


class CacheLoader(ABC):

    @abstractmethod
    def load(self, key):
        pass

    # @abstractmethod
    # def reload(self, key, old_value):
    #     pass

    def load_all(self, keys: Iterable):
        for key in keys:
            self.load(key=key)

    def close(self):
        pass
