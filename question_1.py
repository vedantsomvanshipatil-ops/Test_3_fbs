# 1. Write a program to print first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2
prime_numbers = []

while count < n:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
        count += 1

    num += 1

print(prime_numbers)