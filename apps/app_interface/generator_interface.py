from abc import ABC, abstractmethod

class GeneratorInterface(ABC):
    @abstractmethod
    def __init__(self, args):
        pass

    @abstractmethod
    def bind(self, video_stream):
        pass
    
    @abstractmethod
    def __call__(self, args):
        while True:
            pass

    @abstractmethod
    def generate_task(self, frame):
        pass
