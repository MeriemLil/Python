# Assume this is our secret box
# These are the only two ways to access
list1 = ["Meriem", 1997]
list2 = ["Alla", 1995]

name = input("Enter name: ")

if name == list1[0]:
    code = int(input("Enter code: "))
    if code == list1[1]:
      print("Key 1 Correct. Box Unlocked!")
    else:
      print("Key Name Correct, Key code Wrong!")

elif name == list2[0]:
    code = int(input("Enter code: "))
    if code == list2[1]:
      print("Key 2 Correct. Box Unlocked!")
    else:
      print("Key Name Correct, Key code Wrong!")

else:
    print("Wrong, you have no access!")