num = [1, 2, 3]

for x in num:
    for y in num:
        for z in num:
            if x != y and y != z and z != x:
                print(x, y, z)
            