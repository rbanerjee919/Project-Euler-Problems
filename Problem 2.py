#This program sums all even fibonnaci numbers upto 4 million 
# More efficient method is the first one, much quicker as can be seen in output

#1st method

def fib(max):
    f1, f2 = 0, 1
    while f1 < max:
        yield f1
        f1, f2 = f2, f1 + f2

print(sum(filter(lambda n: n % 2 == 0, fib(4000000))))

#2nd method

def fibonnaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

list_of_fibs = []
i = 1
while fibonnaci(i) < 4*(10**6):
    list_of_fibs.append(fibonnaci(i))
    i += 1

def summer_of_even_fibs():
    return sum(i for i in list_of_fibs if i % 2 == 0)

def run():
    print(summer_of_even_fibs())

if __name__ == "__main__":
    run()
