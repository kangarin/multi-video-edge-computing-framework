from apps.app_interface.integrator_interface import IntegratorInterface

class MyIntegrator(IntegratorInterface):

    def __init__(self, args = None):
        pass

    def __call__(self, args = None):
        import time
        while True:
            print("MyIntegrator call")
            time.sleep(5)
            # 分别汇总多个视频流结果
            pass

    def report_result(self, result = None):
        pass
