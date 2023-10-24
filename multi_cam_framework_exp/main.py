import threading
from queue import Queue
from generator import TaskGenerator
from processor import TaskProcessor
from aggregator import TaskAggregator

def main():
    task_queue = Queue()
    result1_queue = Queue()
    result2_queue = Queue()

    # Start Task Generators
    generator1 = TaskGenerator(id=1, rtsp_url='/Users/wenyidai/GitHub/video-dag-manager/input/input.mov', task_queue=task_queue)
    generator_thread1 = threading.Thread(target=generator1.generate_task)
    generator_thread1.start()

    generator2 = TaskGenerator(id=2, rtsp_url='/Users/wenyidai/GitHub/video-dag-manager/input/input1.mp4', task_queue=task_queue)
    generator_thread2 = threading.Thread(target=generator2.generate_task)
    generator_thread2.start()

    # Start Task Processors (Load Balanced)
    num_processors = 3
    for i in range(num_processors):
        processor = TaskProcessor(task_queue, result_queues=[result1_queue, result2_queue])
        processor_thread = threading.Thread(target=processor.process_task)
        processor_thread.start()

    # Start Task Aggregator
    aggregator1 = TaskAggregator(id=1, result_queue=result1_queue, window_size=5)
    aggregator1_thread = threading.Thread(target=aggregator1.aggregate_results)
    aggregator1_thread.start()

    aggregator2 = TaskAggregator(id=2, result_queue=result2_queue, window_size=5)
    aggregator2_thread = threading.Thread(target=aggregator2.aggregate_results)
    aggregator2_thread.start()

if __name__ == "__main__":
    main()
