# 2. Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!


def sum_of_series(n):
    total = 0
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        total += i / fact

    return total


n = int(input("Enter a number: "))
result = sum_of_series(n)
print(result)