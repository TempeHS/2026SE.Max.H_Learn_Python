num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("what do you want to do? +, -, *, /: ")

answer = 0

if operator == "+":
    answer = num1 + num2
    print(answer)
elif operator == "-":
    answer = num1 - num2
    print(answer)
elif operator == "*":
    answer = num1 * num2
    print(answer)
elif operator == "/":
    answer = num1 / num2
    print(answer)
else:
    print("Invalid operator")