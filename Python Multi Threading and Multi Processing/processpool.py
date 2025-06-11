from concurrent.futures import ProcessPoolExecutor
import time

def print_square(number):
    time.sleep(1)
    return f"Number : {number*number}"

numbers =[1,2,3,4,5,6]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_square,numbers)

    for result in results:
        print(result)