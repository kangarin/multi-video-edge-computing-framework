import cv2
import numpy as np
from queue import Queue
import os

class TaskProcessor:
    def __init__(self, task_queue, result_queues = []):
        self.task_queue = task_queue
        self.result_queues = result_queues

    def process_task(self):
        while True:
            task = self.task_queue.get()
            if task:
                frames = self.extract_frames(task['video_data'], task['id'])
                result = self.process_frames(frames)
                if(task['id'][0] == '1'):
                    self.result_queues[0].put({'id': task['id'], 'avg_gray': result})
                else:
                    self.result_queues[1].put({'id': task['id'], 'avg_gray': result})
                self.task_queue.task_done()

    def extract_frames(self, video_data, task_id):
        # generate a temp file with unique name

        temp_file_path = f'tmp/process_{task_id}.mp4'
        with open(temp_file_path, 'wb') as f:
            f.write(video_data)

        frames = []
        cap = cv2.VideoCapture(temp_file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()

        # Clean up temp file
        os.remove(temp_file_path)

        return frames

    def process_frames(self, frames):
        grays = [self.compute_average_gray(frame) for frame in frames]
        average_grays = np.mean(grays)
        return average_grays

    def compute_average_gray(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        average_gray = np.mean(gray)
        return average_gray

def main():
    task_queue = Queue()
    result_queue = Queue()

    processor = TaskProcessor(task_queue, result_queue)
    processor.process_task()

if __name__ == "__main__":
    main()
