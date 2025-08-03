# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    """A simple calculator to find square, cube, and square root of a number."""

    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num**2

    def cube(self):
        return self.num**3

    def sq_root(self):
        return self.num ** (1 / 2)


print("//---------CALCULATOR---------//")
option = input("Enter what you want (square / cube / square-root): ").strip().lower()

try:
    num = float(input("Enter the number: "))
    calc = Calculator(num)

    if option == "square":
        print(f"Square of {num} is {calc.square()}")
    elif option == "cube":
        print(f"Cube of {num} is {calc.cube()}")
    elif option in ["square-root", "squareroot", "sqrt", "sqroot"]:
        if num < 0:
            print("❌ Cannot calculate square root of a negative number.")
        else:
            print(f"Square root of {num} is {calc.sq_root():.2f}")
    else:
        print("❌ Invalid option selected.")

except ValueError:
    print("❌ Invalid number entered.")
