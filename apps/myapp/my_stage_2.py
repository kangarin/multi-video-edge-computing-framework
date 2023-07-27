from apps.app_interface.stage_interface import StageInterface
class MyStage2(StageInterface):
    def __init__(self, args):
        print("MyStage2 init")

    def __call__(self, args):
        print("MyStage2 call")