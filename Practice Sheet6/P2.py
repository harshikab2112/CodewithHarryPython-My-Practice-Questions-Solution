# Write a program to find out whether a student has passed or failed
# if it requires a total of 40% and at least 33% in each subject to pass.

# Assume 3 subjects and take marks as an input from the user.

sub1 = float(input("Enter the 1st subject marks: "))
sub2 = float(input("Enter the 2nd subject marks: "))
sub3 = float(input("Enter the 3rd subject marks: "))

# Since they are all out of 100.
percent = (sub1 + sub2 + sub3) / 3

if percent >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Pass")
else:
    print("Fail")
