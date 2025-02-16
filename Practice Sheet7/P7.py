# Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter the post: ")

if "harry" in post.lower():
    print("Talking about Harry")
else:
    print("Not talking about Harry")
