# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this".
# Write a program to detect these spams.

comm1 = "Make a lot of money"
comm2 = "buy now"
comm3 = "subscribe this"
comm4 = "click this"

a = input("Enter the comment: ")

if (comm1 in a) or (comm2 in a) or (comm3 in a) or (comm4 in a):
    print("Spam Comment!!")
else:
    print("Not Spam!!")
