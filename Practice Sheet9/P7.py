# Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "rt") as f:
    content = f.readlines()  # this will convert file convert into list.

# Initialize the line counter
line_num = 1

# we will loop through the list
for line in content:
    if "python" in line.lower():
        print(f"'python' found on line {line_num} : {line.strip()}")
        break
    line_num += 1
else:
    print("'python' not found")
