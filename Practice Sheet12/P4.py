# Write a program to display a/b where a and b are integers.
# If b=0, display infinite by handling the 'ZeroDivisionError'.

try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    result = a / b
except ZeroDivisionError:
    print("The result is infinite (division by zero).")
except ValueError:
    print("Invalid input! Please enter integers only.")
else:
    print(f"The result of {a} / {b} is: {result}")
finally:
    print("Program execution completed.")
