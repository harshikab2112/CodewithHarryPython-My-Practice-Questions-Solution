# Write a python function which converts inches to cms.

inch = float(input("Enter in inches: "))


def inches_to_cms(inch):
    cm = inch * 2.54
    return cm


print(f"{inch} inches = {inches_to_cms(inch)} cm")
