# Write a recursive function to calculate the sum of first n natural numbers.


def sum_f_n(num):
    if num == 1:
        return 1
    else:
        return num + sum_f_n(num - 1)


num = int(input("Enter the nth natural number to calculate the sum up to: "))

print(f"Sum of first {num} natural numbers is {sum_f_n(num)}")
