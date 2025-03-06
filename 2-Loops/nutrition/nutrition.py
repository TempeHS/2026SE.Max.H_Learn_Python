fruitdict = {
    "apple": 130,
    "banana": 110,
    }


fruitchoice = input("Enter a fruit: ")
fruitchoice = fruitchoice.lower()
if fruitchoice in fruitdict:
    print(f"Calories in {fruitchoice} is {fruitdict[fruitchoice]}")