# If languages of two friends are same;
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
Enter fav. language: python
Enter name: siya
Enter fav. language: c
Enter name: tiya
Enter fav. language: python
Enter name: niya
Enter fav. language: c++
{'diya': 'python', 'siya': 'c', 'tiya': 'python', 'niya': 'c++'}
"""
# can have same value but can't have same key as it will overwrite the keyvalue
