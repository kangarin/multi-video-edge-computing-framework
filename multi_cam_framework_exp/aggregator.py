from queue import Queue

class TaskAggregator:
    def __init__(self, id, result_queue, window_size):
        self.id = id
        self.result_queue = result_queue
        self.window_size = window_size
        self.result_window = []
        self.expected_id = 0

    def aggregate_results(self):
        while True:
            result = self.result_queue.get()
            if result:
                self.insert_result(result)
                if len(self.result_window) == self.window_size:
                    self.output_results()
                    self.expected_id = int(self.result_window[-1]['id'])
                    self.result_window = []

    def insert_result(self, result):
        idx = 0
        while idx < len(self.result_window) and int(self.result_window[idx]['id']) < int(result['id']):
            idx += 1
        self.result_window.insert(idx, result)

    def output_results(self):
        print(f"Output results with gen && agg id: {self.id}")
        for result in self.result_window:
            if int(result['id']) >= self.expected_id:
                print(f"Processed task {result['id']}, Average gray: {result['avg_gray']}")

def main():
    result_queue = Queue()
    window_size = 5

    aggregator = TaskAggregator(result_queue, window_size)
    aggregator.aggregate_results()

if __name__ == "__main__":
    main()
