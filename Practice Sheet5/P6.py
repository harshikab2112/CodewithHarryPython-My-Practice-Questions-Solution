# Create an empty dictionary.
# Allow 4 friends to enter their favorite language as value and use key as their names.
# Assume that the names are unique.

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
