import math
import time
from tqdm import tqdm


def calculate_Pi(n):
    sign = 1
    Pi = 4
    for i in tqdm(range(n)):
        denominator = (i + 2) * 2 - 1
        sign = sign * (-1)
        Pi = Pi + 4 * sign / denominator
    print(f'calc Pi = {Pi}')
    return Pi


def print_results(Pi, time_s):
    print(f'real Pi = {math.pi}')
    print(f'error = {abs(Pi - math.pi)}')
    print(f'script working time = {time_s:.2f} seconds')


def main():
    n = int(input("enter the iterations number = "))
    time_start = time.time()
    
    if isinstance(n, int):  # if n is not integer print error message
        if n == 0:
            Pi = 4
        else:
            Pi = calculate_Pi(n)
            
    time_spent = time.time() - time_start
    print_results(Pi, time_spent)

    
if __name__ == "__main__":
    main()