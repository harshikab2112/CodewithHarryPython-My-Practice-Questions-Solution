# Write a program to wipe out the content of a file using python.

with open("wipe.txt", "r") as f:
    print("                     *Before Wiping*                     ")
    print(f.read())

with open("wipe.txt", "w") as f:
    f.truncate(0)

"""OR"""

"""with open("wipe.txt", "w") as f:
    pass"""


with open("wipe.txt", "r") as f:
    print("                     *After Wiping*                     ")
    print(f.read())
