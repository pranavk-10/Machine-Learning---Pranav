
## multithreading
## used for i/o bound task and to perform multiple tasks concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)