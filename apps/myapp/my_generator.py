from apps.app_interface.generator_interface import GeneratorInterface
from components.captures.capture_interface import CaptureInterface
import cv2
class MyGenerator(GeneratorInterface):
    def __init__(self, args = None):
        # generate a unique id for this generator
        import uuid
        self.uid = uuid.uuid4()
        self.counter = 0

    def bind(self, capture : CaptureInterface):
        # 绑定到一个视频流
        self.cap = capture
        print("bind to video stream : " + str(self.cap))

    def __call__(self, args = None):
        import time
        import threading
        while True:
            print("MyGenerator call" + threading.currentThread().getName())
            time.sleep(5)
            pass

            # 读取视频
            ret, frame = self.cap.read()
            self.counter += 1
            
            if not ret:
                break
            # 事件检测
            if(self.event_detect(frame)):
                # 生成任务
                self.generate_task(frame)

    def generate_task(self, frame):
        # 放进消息队列
        # cv2.imshow("frame", frame)
        # cv2.waitKey(100000)
        task = {
            "uid": self.uid,
            "frame": frame,
            "counter": self.counter
        }
        print ("generate task : " + str(task))
        return task
    
    def event_detect(self, frame):
        return True