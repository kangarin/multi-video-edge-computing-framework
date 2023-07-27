from apps.app_interface.stage_interface import StageInterface
class MyStage1(StageInterface):
    def __init__(self, args):
        print("MyStage1 init")

    def __call__(self, args):
        print("MyStage1 call")