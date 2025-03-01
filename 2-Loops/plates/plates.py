def main():
		global plate
		plate = input("Plate: ")
		if is_valid(plate):
			print("Valid")
		else:
			print("Invalid")


def is_valid(s):

    chr = (len(plate))

    if chr < 2 or chr > 6:
        print("length")
        return False
	
    for x in range(2):
        if x is str:
            print("start")
            return False
		
    for x in range(2, chr):
        if x is chr:
            
            
	

    return True


main()