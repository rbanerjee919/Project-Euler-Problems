# This program is designed to find the sum of all multiples of 3 or 5 below 1000

def multiples_of_3_and_5(N):
    list_of_num = list(range(1,N))
    care_for_num = []
    for i in list_of_num:
        if (i % 3 == 0) or (i % 5 == 0):
            care_for_num.append(i)
        else:
            continue
    return sum(num for num in care_for_num)

def run():
    print(multiples_of_3_and_5(1000))

if __name__ == "__main__":
    run()
