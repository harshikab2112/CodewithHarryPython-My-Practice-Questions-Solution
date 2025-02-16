# Write a program to print the following star pattern.
# ***
# * *
# *** for n=3

n = 10

for i in range(n):  # row
    for j in range(n):  # column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
