# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

mylist = [10, 17, 20, 24, 30, 52, 55, 60, 38, 40, 45]
maximum = lambda a, b: a if a > b else b
max_val = reduce(maximum, mylist)
print(
    f"Maximum number in the list is {max_val} and its position is {mylist.index(max_val)+1}"
)
