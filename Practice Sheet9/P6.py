# Write a program to mine a log file and find out whether it contains 'python'.

with open("log.txt", "rt") as f:
    content = f.read()

if "python" in content.lower():
    print("The log file contains the word 'python'.")
else:
    print("The word 'python' was not found in the log file.")
