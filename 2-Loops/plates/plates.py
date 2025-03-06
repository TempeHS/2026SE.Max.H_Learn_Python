def main():
	global plate
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(char):

    char = (len(plate))

    if char < 2 or char > 6:
        print("length")
        return False
	
    for chr in range(2):
        if chr is str:
            print("start")
            return False
		
    for chr in range(char, 2):
        if chr is str and chr-1 is int:
            print("middle")
            return False
            
            
	

    return True


main()