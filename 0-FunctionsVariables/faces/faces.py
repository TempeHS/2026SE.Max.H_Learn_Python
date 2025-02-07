def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
converting = input("How are you feeling? ")
print(convert(converting))