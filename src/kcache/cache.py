from abc import ABC, abstractmethod


class Cache(ABC):

    @abstractmethod
    def get_if_present(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def get_all_present(self, keys) -> dict:
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def put_all(self, d: dict) -> None:
        pass

    @abstractmethod
    def invalidate(self, key):
        pass

    @abstractmethod
    def invalidate_all(self, keys):
        pass

    @abstractmethod
    def invalidate_all_elements(self):
        pass

    @abstractmethod
    def size(self):
        pass

    # @abstractmethod
    # def stats(self):
    #     pass

    @abstractmethod
    def as_dict(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass