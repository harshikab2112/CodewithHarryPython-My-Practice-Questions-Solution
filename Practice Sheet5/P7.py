# If the names of 2 friends are same;
# what will happen to the program in problem 6?

myDict = {}
f1 = input("Enter name: ")
l1 = input("Enter fav. language: ")
myDict.update({f1: l1})
f2 = input("Enter name: ")
l2 = input("Enter fav. language: ")
myDict.update({f2: l2})
f3 = input("Enter name: ")
l3 = input("Enter fav. language: ")
myDict.update({f3: l3})
f4 = input("Enter name: ")
l4 = input("Enter fav. language: ")
myDict.update({f4: l4})

print(myDict)

"""
Enter name: diya
Enter fav. language: c
Enter name: niya
Enter fav. language: c++
Enter name: miya
Enter fav. language: c#
Enter name: diya
Enter fav. language: python
{'diya': 'python', 'niya': 'c++', 'miya': 'c#'}"""
# value will be overwritten/updated
