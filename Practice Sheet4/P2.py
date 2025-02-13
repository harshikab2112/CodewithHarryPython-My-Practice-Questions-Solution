# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
f1 = int(input("Enter First student marks here: "))
marks.append(f1)
f2 = int(input("Enter Second student marks here: "))
marks.append(f2)
f3 = int(input("Enter Third student marks here: "))
marks.append(f3)
f4 = int(input("Enter Fourth student marks here: "))
marks.append(f4)
f5 = int(input("Enter Fifth student marks here: "))
marks.append(f5)
f6 = int(input("Enter Sixth student marks here: "))
marks.append(f6)

marks.sort()
print(marks)
