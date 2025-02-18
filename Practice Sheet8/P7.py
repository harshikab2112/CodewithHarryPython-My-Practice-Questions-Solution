# Write a python function to remove a given word from a list and strip it at the same time.

myList = [" Riya ", "  Priya  ", "  Arjun  ", " Miya", "Tiya    "]
target = "Arjun"


def target_remove(myList, target):
    newList = []
    for word in myList:
        if word.strip() != target:
            newList.append(word.strip())
    return newList


print(f"List after target removal and strip: {target_remove(myList,target)}")
