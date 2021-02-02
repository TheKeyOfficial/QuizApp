from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make(self, **kwargs):
        raise NotImplementedError
