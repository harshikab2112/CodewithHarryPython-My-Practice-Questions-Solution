# Write a python program to rename a file to "renamed_by_python.txt".

import os

old_name = "old_file.txt"

new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)

print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
