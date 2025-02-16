# Attempt problem 1 using while loop.

n = int(input("Enter a number to get its multiplication table: "))

i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1
