#ask user for name then Removes whitespace from str and capatalise
name = input('Whats your name? ').strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello with their given name
print(f"hello, {name}")