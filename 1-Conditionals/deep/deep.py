answer = input("What is the meaning of life? ")

answer = answer.lower()

if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("Yes")
elif answer == "forty-two":
    print("yes")
else:
    print("N0")