camel_case = input("Give me camels! ")
snake_case = ""
# finds all capitals in a sentence
for chr in camel_case:
    if chr.isupper():
        snake_case = "_" + chr.lower()
    else:
        snake_case += chr
        

print(snake_case)

