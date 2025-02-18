# Write a python function to print first n lines of the following pattern:
# ***
# **  - for n = 3
# *

num = int(input("Give number of lines: "))


def print_star(num):
    for i in range(num, 0, -1):
        print("*" * i)


print_star(num)
