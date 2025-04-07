#crete 2 lists of items
list1 = []
list2 = []
dict1 = (list1, list2)
#print the lists as a table
with open("textfile.csv", "r")as file:
    lines = file.readlines()

with open("names.csv") as file:
    row = lines

print(f"| col 1 | col 2 |" )
print("| ----- | ----- |")
for i in range(len(row)):
    print(f"{row[i]}")
    
#user inpurt a item to a prompt and only the name from the table prints
def corrospond():
    try:
        input1 = input("Product: ")
        pos1 = dict1.index(input1)
        corrorsponding = dict1[pos1]
        if input1 in list1 or input1 in list2:
            print(f"{input1} and {corrorsponding}")
        else:
            print("dfdhg")
    except ValueError:
        print("not in list")
    else:
        False


corrospond()
#add a new item and sort the list
yupornah = input("Add an item; Y/N: ").lower()
inputlist1:str
inputlist2:str
if yupornah == 'y':
    inputlist1 = input("Item Name: ")
    if inputlist1 in dict1:
        False
    else:
        list1.append(inputlist1)
    inputlist2 = input("Corrosponding Name: ")
    list2.append(inputlist2)


#create a text document with the lists

with open("textfile.csv", "a") as file:
    file.write(str(dict1))
    file.write("\n")
#read from the lists
with open("textfile.csv") as file:
    for i in range(len(list1)):
        print(f"| {list1[i]} | {list2[i]} |")
#edit lines and write to lists
