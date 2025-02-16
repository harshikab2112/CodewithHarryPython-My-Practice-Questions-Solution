# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Please enter a valid positive number.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
