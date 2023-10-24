import cv2
import time
import threading
import numpy as np
from queue import Queue
import os

class TaskGenerator:
    def __init__(self, id, rtsp_url, task_queue):
        self.id = id
        self.rtsp_url = rtsp_url
        self.task_queue = task_queue
        self.counter = 0

    def generate_task(self):
        cap = cv2.VideoCapture(self.rtsp_url)
        while cap.isOpened():
            frames = []
            while len(frames) < 50:
                ret, frame = cap.read()
                if not ret:
                    break
                frames.append(frame)

            if frames:
                task_id = f"{self.id}_{self.counter}"
                self.counter += 1
                compressed_video = self.compress_frames(frames)
                task = {
                    'id': task_id,
                    'video_data': compressed_video
                }
                self.task_queue.put(task)

    def compress_frames(self, frames):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        height, width, _ = frames[0].shape
        out = cv2.VideoWriter(f'tmp/task_{self.id}_{self.counter}.mp4', fourcc, 30, (width, height))
        for frame in frames:
            out.write(frame)
        out.release()
        with open(f'tmp/task_{self.id}_{self.counter}.mp4', 'rb') as f:
            compressed_video = f.read()
        # delete the temporary file
        os.remove(f'tmp/task_{self.id}_{self.counter}.mp4')
        return compressed_video

def main():
    task_queue = Queue()
    generator1 = TaskGenerator(id=1, rtsp_url='/Users/wenyidai/GitHub/video-dag-manager/input/input.mov', task_queue=task_queue)
    generator_thread1 = threading.Thread(target=generator1.generate_task)
    generator_thread1.start()

if __name__ == "__main__":
    main()
