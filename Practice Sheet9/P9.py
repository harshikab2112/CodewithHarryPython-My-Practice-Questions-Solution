# Write a program to find out whether a file is identical & matches the content of another file.

# Read the content of the first file
with open("this.txt", "rt") as f:
    file_content_1 = f.read()

# Read the content of the second file
with open("this_copy.txt", "rt") as f:
    file_content_2 = f.read()

# Compare both contents
if file_content_1 == file_content_2:
    print("Files are identical and content is the same.")
else:
    print("Files are not identical and content is not the same.")
