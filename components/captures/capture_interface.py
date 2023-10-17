from abc import ABC, abstractmethod

class CaptureInterface(ABC):
    @abstractmethod
    def __init__(self, config):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def info(self):
        pass

