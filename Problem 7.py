from itertools import count
import time

def primes_list():
    start = time.time()
    l_o_p = []
    for i in count(2):
        if all(map(lambda prime: i % prime, l_o_p)):
            l_o_p.append(i)
        else:
            continue
        if len(l_o_p) > 10000:
            break
    duration = time.time() - start
    return l_o_p[10000],duration,len(l_o_p)
            
def run():
    print(primes_list())

if __name__ == "__main__":
    run()
