# Write a program to make a copy of a text file "this.txt".

# Open the original file in read mode
with open("this.txt", "rt") as f:
    content = f.read()

# Create a new file and write the same content to it
with open("this_copy.txt", "w") as f:
    f.write(content)
