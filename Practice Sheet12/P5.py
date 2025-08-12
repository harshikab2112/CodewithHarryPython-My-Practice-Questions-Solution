# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

user_input = int(input("Enter a number to generate its multiplication table: "))

table = [f"{user_input} X {i} = {user_input*i}" for i in range(1, 11)]
content = "\n".join(table)
with open("Tables.txt", "w") as file:
    file.write(content)

print(f"Multiplication table for {user_input} has been written to Tables.txt.")

while True:
    display = (
        input("Do you want to display the multiplication table? (yes/no): ")
        .strip()
        .lower()
    )
    if display == "yes":
        with open("Tables.txt", "r") as file:
            print(file.read())
        break
