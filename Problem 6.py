#This is to find the difference between the sum of the squares and the square of the sum of the first 100 numbers

def diff_sum_sqaure_business():
    sum_of_squares = sum([i**2 for i in range(1,101)])
    square_of_sum = (sum(list(range(1,101))))**2
    return square_of_sum - sum_of_squares

def run():
    print(diff_sum_sqaure_business())

if __name__ == "__main__":
    run()