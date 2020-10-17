from kcache.cache_builder import CacheBuilderImpl
from kcache.cacheloader import CacheLoader


class MyCacheLoader(CacheLoader):
    def load(self, key: int):
        return str(key + 1)


def test_cache_growth():
    cache = CacheBuilderImpl().loader(loader=MyCacheLoader()).build()
    assert cache.size() == 0
    assert cache.get(1) == "2"
    assert cache.size() == 1
    assert cache.get(1) == "2"
    assert cache.size() == 1
    assert cache.get(2) == "3"
    assert cache.size() == 2


if __name__ == '__main__':
    test_cache_growth()
