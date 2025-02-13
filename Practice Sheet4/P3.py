# Check that a tuple cannot be changed in python.

myTuple0 = ("Mary", "Larry", 90)
myTuple0[1] = "Carry"
print(myTuple0)

# Check that a tuple type can be changed or not in python.

myTuple1 = ("Mary", 78, 90, True, 35 + 3j)

myList1 = list(myTuple1)

print(myList1)
print(type(myList1))
