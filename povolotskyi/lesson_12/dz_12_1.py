import concurrent.futures
import time

NUMBERS = [3, 7, 21, 27, 33]

def factorial(n):
    if n > 1:
        x = factorial(n - 1) * n
    else:
        return 1
    return x

def ThreadPool():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_thread = executor.map(factorial, NUMBERS)
        # for result_thread in future_thread:
        #     print(result_thread)

def ProcessPool():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        future_process = executor.map(factorial, NUMBERS)
        # for result_process in future_process:
        #     print(result_process)

if __name__ == '__main__':
    start_thread = time.time()
    ThreadPool()
    end_thread = time.time()
    time_thread = end_thread - start_thread

    start_process = time.time()
    ProcessPool()
    end_process = time.time()
    time_process = end_process - start_process

    if float(time_process) > float(time_thread):
        print("ThreadPoolExecutor is better")
    else:
        print("ProcessPoolExecutor is better")