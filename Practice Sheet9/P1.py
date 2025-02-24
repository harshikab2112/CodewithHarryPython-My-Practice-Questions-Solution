# Write a program to read the text from a given file 'poems.txt'
# and find out whether it contains the word 'twinkle'.

with open("poems.txt", "rt") as f:
    data = f.read().lower()

if "twinkle" in data:
    print("Exist")
else:
    print("Doesn't Exist")
