#crete 2 lists of items
# list1 = []
# list2 = []
# dict1 = (list1, list2)
#print the lists as a table
# best to use 2 lists instead of a dictionary to make things less complicated :)
list1 = []
list2 = []

# iterates through the index of one of the lists
for item in range(len(list1)):
    # prints it out nicely
    print(f"{list1[item]} | {list2[item]}")

# with open("textfile.csv", "r")as file:
#     key, value = file.readlines()

# with open("names.csv") as file:
#     row = lines

# print(f"| col 1 | col 2 |" )
# print("| ----- | ----- |")
# for i in range(len(row)):
#     print(f"{row[i]}")
    
# #user inpurt a item to a prompt and only the name from the table prints
# def corrospond():
#     try:
#         input1 = input("Product: ")
#         pos1 = dict1.index(input1)
#         corrorsponding = dict1[pos1]
#         if input1 in dict1:
#             print(f"{input1} and {corrorsponding}")
#         else:
#             print("dfdhg")
#     except ValueError:
#         print("not in list")
#     else:
#         False



#add a new item and sort the list
yupornah = input("Add an item; Y/N: ").lower()
inputlist1:str
inputlist2:str
if yupornah == 'y':
    inputlist1 = input("Item Name: ")
    list1.append(inputlist1)
    inputlist2 = input("Corrosponding Name: ")
    list2.append(inputlist2)
else:
    False

with open("textfile.csv", "r")as file:
    # this reads each line and appends the content in "line" variable
    for line in file:
        # this splits and cleans up the rubbish: 
        # OLD: 'diddy': ' babyoil\n'
        # NEW: diddy, babyoil
        split = line.replace("\n", "").replace(" ", "").split(',')
        # makes it easier for viewing, not required
        key = split[0]
        value = split[1]
        # append to each list
        list1.append(key)
        list2.append(value)
#create a text document with the lists
for item in range(len(list1)):
    # prints it out nicely
    print(f"{list1[item]} | {list2[item]}")


with open("textfile.csv", "a") as file:
    for index in range(len(list1)):
        file.write(f"{list1[index]}, {list2[index]}")
        file.write("\n")
#read from the lists
with open("textfile.csv") as file:
    for i in range(len(list1)):
        print(f"| {list1[i]} | {list2[i]} |")
#edit lines and write to lists
