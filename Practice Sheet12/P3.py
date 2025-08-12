# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

user_input = int(input("Enter a number to generate its multiplication table: "))

table = [f"{user_input} X {i} = {user_input*i}" for i in range(1, 11)]
print("\n".join(table))
