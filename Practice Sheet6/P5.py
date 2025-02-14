# Write a program which finds out whether a given name is present in a list or not.

myList = ["Ria", "Mia", "Tia", "Pia", "Sia", "Nia", "Lia"]
a = input("Enter a name: ")

if a.capitalize() in myList:
    print("Present")
else:
    print("Not Present")
