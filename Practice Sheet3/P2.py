# Write a program to fill in a letter template
# given below with name and date.
# letter = """
# Dear <Name>,
# You are selected!
# </Date|>
# """

name = input("Enter your name: ")
date = input("Enter current date: ")

letter = f"""
    Dear {name}, 
    You are selected! 
    {date}
"""
print(letter)

# Using string chaining
Letter = """
    Dear <Name>,
    You are selected!
    </Date|>
"""

print(Letter.replace("<Name>", "Tushar").replace("</Date|>", "28.June.2024"))
