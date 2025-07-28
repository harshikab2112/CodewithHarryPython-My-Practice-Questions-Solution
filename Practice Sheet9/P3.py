# Write a program to generate multiplication tables from 2 to 20 and
# write it to the different files.
# Place these files in a folder for a 13-year old.

import os


def multiplication_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables_for_kids/table_{n}.txt", "w") as f:
        f.write(table)


# Create folder if it doesn't exist
os.makedirs("tables_for_kids", exist_ok=True)

# Generate tables from 2 to 20
for i in range(2, 21):
    multiplication_table(i)
