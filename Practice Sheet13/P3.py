# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

mylist = [7 * i for i in range(1, 11)]

print("\n".join(map(str, mylist)))
