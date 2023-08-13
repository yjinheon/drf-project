import time
import os
import threading

nums = [50, 63, 32]

import sys

# int max str digits
#sys.set_int_max_str_digits(10000)

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k

    return total


def main():
    results = [cpu_bound_func(num) for num in nums]
    print(results)


if __name__ == "__main__":
    sys.set_int_max_str_digits(10000)
    start = time.time()
    main()
    end = time.time()
    print(f"Total time: {end-start}")
