# Write a program to find the greatest of four numbers entered by the user.

a = float(input("Enter first no. : "))
b = float(input("Enter second no. : "))
c = float(input("Enter third no. : "))
d = float(input("Enter fourth no. : "))

if a >= b and a >= c and a >= d:
    print(f"{a} is greatest of all four.")
elif b >= c and b >= d and b >= a:
    print(f"{b} is greatest of all four.")
elif c >= d and c >= a and c >= b:
    print(f"{c} is greatest of all four.")
else:
    print(f"{d} is greatest of all four.")
