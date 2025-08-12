# Write a program to print third, fifth and seventh element from a list using enumerate function.

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(mylist, start=1):
    if index in [3, 5, 7]:
        print(f"The {index}th element is {value}")
