camel_case = input("Give me camels! ")
snake_case = ""
# finds all capitals in a sentence
for chr in camel_case:
    if chr.isupper():
        snake_case = chr + "_" chr.lower()
        

print(camel_case)