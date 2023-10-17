# change cur dir to root path of the project
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from apps.myapp import my_generator
from components.captures.camera_capture import CameraCapture
from components.captures.file_capture import FileCapture
import cv2

if __name__ == '__main__':
    # config = {
    #     # "video_path": "/Volumes/Untitled/video/ixpe.mp4"
    #     "video_path": 0
    # }
    # # 生成器
    # generator = my_generator.MyGenerator(config)
    # generator()

    # cap = CameraCapture({"camera_id": 0})
    # while True:
    #     frame = cap.read()
    #     if frame is None:
    #         break
    #     cv2.imshow("frame", frame)
    #     cv2.waitKey(1)
    # cv2.destroyAllWindows()

    cap = FileCapture({"video_file_path": "/Volumes/Untitled/video/ixpe.mp4"})

    while True:
        frame = cap.read()
        if frame is None:
            break
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()