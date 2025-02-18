# Write a python function to print multiplication table of a given number.

n = int(input("Enter a number to get its multiplication table: "))


def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


table(n)
