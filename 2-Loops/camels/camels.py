camel_case = input("Give me camels! ")
snake_case = ""
# finds all capitals in a sentence
for char in camel_case:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
        

print(snake_case)

