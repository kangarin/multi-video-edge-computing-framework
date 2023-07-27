from apps.app_interface.stage_interface import StageInterface
class MyStage4(StageInterface):
    def __init__(self, args):
        print("MyStage4 init")

    def __call__(self, args):
        print("MyStage4 call")