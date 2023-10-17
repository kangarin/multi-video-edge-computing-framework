from abc import ABC, abstractmethod
from components.captures.capture_interface import CaptureInterface

class GeneratorInterface(ABC):
    @abstractmethod
    def __init__(self, args):
        pass

    @abstractmethod
    def bind(self, capture : CaptureInterface):
        # video_stream should be of type CaptureInterface
        pass
    
    @abstractmethod
    def __call__(self, args):
        while True:
            pass

    @abstractmethod
    def generate_task(self, frame):
        pass
