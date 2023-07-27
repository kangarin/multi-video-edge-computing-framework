from abc import ABC, abstractmethod

class StageInterface(ABC):
    @abstractmethod
    def __init__(self, args):
        pass

    @abstractmethod
    def __call__(self, args):
        pass