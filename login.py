#menu
def login():
    menu_choice = input("login: 1\nregister: 2\nexit: 3\nchoice: ")
    if menu_choice == "1":
        #asks for username then checks file to confirm exists
        login_username = input("please enter username: ")
        listofuser = []
        listofpassword = []
        #appends all usernames from file into list to compare
        with open("logins.csv") as file:
            for lines in file:
                username, password = lines.strip().split(",")
                listofuser.append(username.strip())
                listofpassword.append(password.strip())
        #checks for username in the list of usernames
        if login_username in listofuser:
            login_password = input("success, now password: ")
            try:
                index = listofuser.index(login_username)
                # print(login_username)
                # print(listofuser[index])
                # print(login_password)
                # print(listofpassword[index])
                #checks for password at the index of the username
                if login_password == listofpassword[index]:
                    #ask for either password change or exit
                    print("success")
                    login_option = input("Change password: 1\nexit: 2\nchoice: ")
                    if login_option == "1":
                        new_password = input("New password: ")
                        readLines=[]
                        #change password at index of username for list
                        with open("logins.csv") as file:
                            for line in file:
                                if login_username not in line.split(',')[0]:
                                    readLines.append(line)
                            readLines.append(f"{login_username}, {new_password}")
                        with open("logins.csv", "w") as file:
                            for item in readLines:
                                file.write(item)
                        print("Done!") 
                else:
                    print("password incorrect")
            except(ValueError):
                print("password not found")
        else:
            print("username not found")
    elif menu_choice == "2":
        #call for register
        register()
    elif menu_choice == "3":
            exit()
    else:
        print("please choose valid option")

def register():
    register_username = input("enter new username: ")
    regsiter_password = input("enter new password: ")
    with open("logins.csv", "a") as file:
        file.write(f"{register_username}, {regsiter_password}\n")
    decode()

def decode():
    with open("logins.csv", "r") as file:
        for line in file:
            line = line.strip()
            username, password = line.split(", ")
            print(f"username: {username}, password: {password}")
login()

def thingymabob():
    listOfUsers = []
    listOfPasswords = []
    file = open("logins.csv", "r")
    for line in file:
        line = line.strip()
        username, password = line.split(", ")
        listOfUsers.append(username)
        listOfPasswords.append(password)
    option = input("Input username:")
    if option in listOfUsers:
        print("Username found")
        index = listOfUsers.index(option)
        optionPass = input("Whats your password")
        if optionPass == listOfPasswords[index]:
            print("Password found, successfully authed")