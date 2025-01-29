# WAP to print the contents of a directory using os module.
# Search online for a function which does that.

import os

# List all files and folders in the current directory
contents = os.listdir()

# Print the contents
print("Contents of the current directory:")
for item in contents:
    print(item)
