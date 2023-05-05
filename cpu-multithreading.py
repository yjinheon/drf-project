import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


nums = [58, 62, 32]


def cpu_bound(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread,{num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    # multi-threading
    results = list(executor.map(cpu_bound, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Total time: {end-start}")
