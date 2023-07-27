from abc import ABC, abstractmethod

class IntegratorInterface(ABC):
    @abstractmethod
    def __init__(self, args):
        pass

    @abstractmethod
    def __call__(self, args):
        while True:
            # 分别汇总多个视频流结果
            pass

    @abstractmethod
    def report_result(self, result):
        pass
