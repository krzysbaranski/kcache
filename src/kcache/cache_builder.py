from abc import ABC, abstractmethod

from kcache.cache import Cache
from kcache.cacheloader import CacheLoader
from kcache.loading_cache import LoadingCache


class CacheBuilder(ABC):

    @abstractmethod
    def build(self) -> Cache:
        pass

    @abstractmethod
    def loader(self, loader: CacheLoader):
        pass


class CacheBuilderImpl(CacheBuilder):
    def __init__(self) -> None:
        pass

    def build(self) -> Cache:
        return LoadingCache(loader=self._loader)

    def loader(self, loader: CacheLoader):
        self._loader = loader
        return self

    def removal_listener(self, listener) -> CacheBuilder:
        raise NotImplemented()
        # return self

    def refresh_after_write(self, duration_ms: int) -> CacheBuilder:
        raise NotImplemented()
        # return self

    def expire_after_access(self, duration_ms: int) -> CacheBuilder:
        raise NotImplemented()
        # return self

    def expire_after_write(self, duration_ms: int) -> CacheBuilder:
        raise NotImplemented()
        # return self

    def maximum_size(self, maximum_size: int) -> CacheBuilder:
        raise NotImplemented()
        # return self
