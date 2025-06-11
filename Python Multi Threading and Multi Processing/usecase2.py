import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(10000)

#function to compute factorial

def factorial(n):
    print(f"Computing the factorial of {n}:")
    sys.set_int_max_str_digits(10000)
    result = math.factorial(n)
    print(f"The factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers = [50,60,700,300]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial,numbers)
    
    end_time = time.time()

    print(f"Results : {results}")
    print(f"Total Time Taken : {end_time - start_time} seconds")