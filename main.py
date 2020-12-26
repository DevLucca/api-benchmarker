import os
import sys
import json
import time
from datetime import datetime
from parallel_tests import StartParallel
from sequential_tests import StartSequential

def main():
    with open("tests.json", "r", encoding="utf-8") as f:
        tests = json.load(f)
    
    results = dict()
    for test in tests:
        results['-'.join(test['name'].split(' ')).lower()] = []

    for test in tests:
        test_name = '-'.join(test['name'].split(' ')).lower()
        print(f"""----------------------------------------------
        \rInitializing Test: {test['name']}
        \r----------------------------------------------""")
        for config in test['config']:
            if config['method'] == "parallel":
                results[test_name].append({
                    "method": config['method'],
                    "test-results": StartParallel(**config).run()
                })
            elif config['method'] == "sequential":
                results[test_name].append({
                    "method": config['method'],
                    "test-results": StartSequential(**config).run()
                })
            else:
                print(f"Unkown test method: {config['method']}")
        
        with open(f"results/{datetime.now().strftime('%Y-%m-%d_%H.json')}", "w") as f:
            json.dump(results, f, indent=4, sort_keys=True)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"--- Total of {round(end_time - start_time, 2)} seconds to run all tests ---")