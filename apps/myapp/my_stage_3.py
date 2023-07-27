from apps.app_interface.stage_interface import StageInterface
class MyStage3(StageInterface):
    def __init__(self, args):
        print("MyStage3 init")

    def __call__(self, args):
        print("MyStage3 call")