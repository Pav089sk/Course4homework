from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class Named(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
