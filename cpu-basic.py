import time
import os
import threading

nums = [50,63,32]

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1,num)
    total = 1
    for i in numbers