# Write a program to filter a list of numbers which are divisible by 5.

mylist = [10, 17, 20, 24, 30, 38, 40, 45, 52, 55, 60]

divisible_5 = lambda x: x % 5 == 0

print(list(filter(divisible_5, mylist)))
