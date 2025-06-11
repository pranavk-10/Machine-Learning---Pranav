## multiprocessing
## allows you to create multiple processes
## cpu - bound tasks and use multiple cores of cpu

import multiprocessing
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i}*{i} = {i*i}")

def cube():
    for i in range(5):
        time.sleep(1)
        print(f"Cube : {i}*{i}*{i} = {i*i*i}")\
        
if __name__ == "__main__":

    p1= multiprocessing.Process(target=square)
    p2= multiprocessing.Process(target=cube)

    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)