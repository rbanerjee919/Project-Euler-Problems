#This program is designed to find the largest palindromic number that is the product of two 3 digit-numbers.

def check_palindrome(n):
    val = str(n)
    if val == str(n)[::-1]:
        return True
    else:
        return False


def largest_panlindrome_n_digit_product(n):
    i = (10**n) - 1
    j = (10**n) - 1
    count = 0
    while check_palindrome(i*j) == False:
        j -= 1
        count += 1
        if count % (10**(n-1)) == 0:
            i -= 1
            j = (10**n) - 1
    else:
        return i*j,i,j

def run():
    print(largest_panlindrome_n_digit_product(5))

if __name__ == "__main__":
    run()