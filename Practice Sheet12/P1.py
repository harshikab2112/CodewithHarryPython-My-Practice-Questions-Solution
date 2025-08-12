# Write a program to open three files 1.txt, 2.txt and 3.txt
# if any these files are not present,
# a message without exiting the program must be printed prompting the same.

files = ["1.txt", "2.txt", "3.txt"]

for filename in files:
    print(f"Checking for {filename}...")
    try:
        with open(filename, "r") as f:
            print(f"Content of {filename}:")
            print(f.read().strip())  # strip() removes trailing spaces/newlines
    except FileNotFoundError:
        print(f"Error: {filename} not present.")
    print("-" * 40)  # separator line

print("\nProgram completed without exiting.\nThank you!")
