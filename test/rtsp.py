import os
import cv2
import gc
import time
import threading
import numpy as np
from PIL import Image

top = 100

stack = []


# 向共享缓冲栈中写入数据:
def write(stack, cam, top: int) -> None:
    """
    :param cam: 摄像头参数
    :param stack: list对象
    :param top: 缓冲栈容量
    :return: None
    """
    print('Process to write: %s' % os.getpid())
    cap = cv2.VideoCapture(cam)
    while True:
        _, img = cap.read()
        if _:
            stack.append(img)
            print(stack)
            # 每到一定容量清空一次缓冲栈
            # 利用gc库，手动清理内存垃圾，防止内存溢出

            if len(stack) >= top:
                del stack[:]
                gc.collect()


# 在缓冲栈中读取数据:
def read(stack) -> None:
    print('Process to read: %s' % os.getpid())
    # 开始时间
    t1 = time.time()
    # 图片计数
    count = 0

    while True:
        if len(stack) != 0:
            # 开始图片消耗
            print("stack的长度", len(stack))
            if len(stack) != 100 and len(stack) != 0:
                value = stack.pop()
            else:
                pass

            if len(stack) >= top:
                del stack[:]
                gc.collect()

            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(value, cv2.COLOR_BGR2RGB)
            # # 转变成Image
            frame = Image.fromarray(np.uint8(frame))

            print("*" * 100)

            count += 1
            print("数量为：", count)

            t2 = time.time()
            print("时间差：", int(t2 - t1))

            if int(t2 - t1) == 600:
                # 记录 消耗的图片数量
                with open('count.txt', 'ab') as f:
                    f.write(str(count).encode() + "\n".encode())
                    f.flush()

                # count = 0  # 不要置零，计算总数
                t1 = t2


if __name__ == '__main__':
    for i in range(1):
        thread_pro = threading.Thread(target=write, args=(stack, "rtsp://localhost:8554/mystream", top,))
        thread_pro.start()

    for j in range(3):
        thread_con = threading.Thread(target=read, args=(stack,))
        thread_con.start()
