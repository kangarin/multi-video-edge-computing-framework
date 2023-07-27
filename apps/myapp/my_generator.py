from apps.app_interface.generator_interface import GeneratorInterface
import cv2
class MyGenerator(GeneratorInterface):
    def __init__(self, args = None):
        # generate a unique id for this generator
        import uuid
        self.uid = uuid.uuid4()
        self.counter = 0

    def bind(self, video_stream):
        # 绑定到一个视频流
        self.video_stream = video_stream
        print("bind to video stream : " + str(video_stream))

    def __call__(self, args = None):
        while True:
            # 读取视频
            ret, frame = self.cap.read()
            
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
        return task
    
    def event_detect(self, frame):
        return True