equation = input("arimatic equation? ")

x, y, z = equation.split()

x = float(x)
z = float(z)

if "+" in equation:
    print(x+z)
elif "-" in equation:
    print(x-z)
elif "*" in equation:
    print(x*z)
elif "/" in equation:
    print(x/z)