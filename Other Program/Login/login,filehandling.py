import json

def registration():
    print("Register Account")
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    f = open("Other Program/Login/user_db.txt",'r')
    a = f.read()
    list_user = a.split('-')
    for i in list_user:
        if i != '':
            aa = json.loads(i)
            if username in aa:
                return print("Username Exist")
    
    user = {username: password}
    f = open("Other Program/Login/user_db.txt",'a')
    f.write(json.dumps(user) + "-")
    f.close()
    print("Register Sucessfull")


def login():
    print("Login")
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    f = open("Other Program/Login/user_db.txt",'r')
    a = f.read()
    list_user = a.split('-')
    for i in list_user:
        if i != '':
            aa = json.loads(i)
            if username in aa:
                if aa[username] == password:
                        print("Login Sucessful")
                        
                        while True:
                            choice = input("Do you want to logout? (yes/no): ")
                            if choice.lower() == "yes":
                                return
                            elif choice.lower() == "no":
                                continue
                            else:
                                print("Invalid choice. Please enter 'yes' or 'no'.")
                else:
                    return print("Invalid Password")
    print("Username not found")
          
    f.close()

def main():
    while True:
        print("Menu\n1. Register 2. Login 3. Exit")
        choice = input("Enter Your Choice : ")
        if choice == "1":
            registration()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank You for using this system")
            exit()
        else:
            print("Invalid Command")
main()