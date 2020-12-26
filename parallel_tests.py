from datetime import datetime
import threading
import requests
import concurrent.futures


class StartParallel:

    endpoint = str()
    test_count = int()

    def __init__(self, endpoint, test_count, **kwargs):
        print(f"Paralel testing on \"{endpoint}\" with {test_count} requests")
        self.endpoint = endpoint
        self.test_count = test_count

    def run(self):
        elapsed_time = []
        for i in range(self.test_count):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.run_requests)
                return_value = future.result()
                elapsed_time.append(return_value)
        return sum(elapsed_time) / len(elapsed_time)

    def run_requests(self):
        response = requests.get(self.endpoint)
        return response.elapsed.total_seconds()