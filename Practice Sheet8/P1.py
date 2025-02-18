# Write a program using functions to find greatest of three numbers.

a = float(input("Enter first no. : "))
b = float(input("Enter second no. : "))
c = float(input("Enter third no. : "))


def greatest_number(a, b, c):
    if a >= b and a >= c:
        return f"{a} is greatest of all three."
    elif b >= c and b >= a:
        return f"{b} is greatest of all three."
    else:
        return f"{c} is greatest of all three."


print(greatest_number(a, b, c))
