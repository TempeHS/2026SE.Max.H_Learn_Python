while true:
    try:
        #ask for fraction
        fraction = input("Enter a fraction: ")
        #split the fraction
        num, den = fraction.split("/")
        #convert to float
        percentage = float(num) / float(den) * 100
        #ifs
        if percentage < 1/100:
            print("E")
        elif percentage > 99/100:
            print("F")
except ValueError:
    return False

