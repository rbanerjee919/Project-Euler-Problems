# The objective is to find the greatest prime factor of 600851475143

import time

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def check_if_prime(n):
    if n == 1:
        return False
    
    i = 2
    while (i**2) <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    


def greatest_prime_factor(n):
    start = time.time()
    list_of_factors_of_n = factors(n)
    list_of_prime_factors_of_n = []
    for j in list_of_factors_of_n:
        if check_if_prime(j) == True:
            list_of_prime_factors_of_n.append(j)
        else:
            continue
    duration = time.time() - start
    return sorted(list_of_prime_factors_of_n)[-1:],duration


def run():
    print(greatest_prime_factor(600851475143))

if __name__ == "__main__":
    run()

