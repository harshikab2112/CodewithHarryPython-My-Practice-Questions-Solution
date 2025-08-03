# Create a class with a class attribute a;
# create an object from it and set 'a' directly using object.a = o.
# Does this change the class attribute?


class demo:
    a = 4


o = demo()
print(o.a)  # prints the class attribute because instance attribute is not present

o.a = 0  # Instance attribute is set now
print(o.a)  # print the instance attribute because instance attribute is present

print(demo.a)  # Still prints 4
"""
No. The class attribute remains unchanged.
"""
