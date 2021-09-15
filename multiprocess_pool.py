
from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print(f"Run task {name} ({os.getpid()})")
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f"Task {name} {end - start} seconds.")


if __name__ == "__main__":
    print(f"Parent process {os.getpid()}")
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all subproesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")
