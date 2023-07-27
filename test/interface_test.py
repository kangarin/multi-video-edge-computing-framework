# change cur dir to root path of the project
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from apps.myapp import my_generator

if __name__ == '__main__':
    config = {
        # "video_path": "/Volumes/Untitled/video/ixpe.mp4"
        "video_path": 0
    }
    # 生成器
    generator = my_generator.MyGenerator(config)
    generator()