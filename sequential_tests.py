import requests

class StartSequential:

    endpoint = str()
    test_count = int()

    def __init__(self, endpoint, test_count, **kwargs):
        print(f"Sequential testing on \"{endpoint}\" with {test_count} requests")
        self.endpoint = endpoint
        self.test_count = test_count
        self.run()

    def run(self):
        elapsed_time = []
        for i in range(self.test_count):
            response = requests.get(self.endpoint)
            elapsed_time.append(response.elapsed.total_seconds())
        return sum(elapsed_time) / len(elapsed_time)