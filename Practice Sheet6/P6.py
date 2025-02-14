# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 =>Ex
# 80 - 90 =>A
# 70 -80 =>B
# 60 - 70 =>C
# 50-60 => D
# < 50 =>F

a = int(input("Enter student marks: "))

if 90 <= a <= 100:
    print("Excellent")
elif 80 <= a < 90:
    print("A")
elif 70 <= a < 80:
    print("B")
elif 60 <= a < 70:
    print("C")
elif 50 <= a < 60:
    print("D")
else:
    print("F")
