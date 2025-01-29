# Label the program written in P4 with comments.

# importing os module
import os

# List all files and folders in the current directory
contents = os.listdir()

# Print the contents
print("Contents of the current directory:")
for item in contents:
    print(item)
