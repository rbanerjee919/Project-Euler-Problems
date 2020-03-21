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

def prime_factors_below_n(n):
    list_of_primes = [i for i in range(2,n+1) if check_if_prime(i) == True]
    return list_of_primes

#Method is way way too slow (waited 10 min)

#def div_by_one_to_twenty():
    #n = 20
    #one_to_twenty = list(range(1,21))
    #while set(one_to_twenty).issubset(factors(n)) == False:
        #n += 1
    #else:
        #return n


from itertools import count, takewhile

def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1)))) #From number theory
        print(list(takewhile(lambda x:x<=n, (prime ** c for c in count(1)))))
        # we could just take last instead of max()
        result *= bprime
    return result


def run():
    
    print(smallest(20))
    print(list(range(1,11)))
    print(prime_factors_below_n(20))

if __name__ == "__main__":
    run()