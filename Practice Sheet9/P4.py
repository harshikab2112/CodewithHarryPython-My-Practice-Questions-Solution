# A file contains a word "Donkey" multiple times.
# You need to write a program which replace this word with ##### by updating the same file.

with open("P4.txt", "rt") as f:
    data = f.read().lower()

data = data.replace("donkey", "#####")

with open("P4.txt", "w") as f:
    f.write(data)

with open("P4.txt", "rt") as f:
    data = f.read()
    print(data)
