# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
