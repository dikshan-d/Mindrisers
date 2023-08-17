#make variable that store user username and password and set value empty and make that in dictionary
#System Register, Login , Show Registered Users and Make Exit
# Take input of username and password and user .strip() in loop check the username exist or not otherwise append in empty variable and print registered sucess
# Take input if user exist login and make logout or return to menu other wise invalid choice and other wise invalid password if passsword wronng other wisr user not found
# print register username and password use f format
# Exit Program other wise invalid choice

user = [{'Username':'','Password':''}]
rerun = True
while rerun:
    print("Welcome to Registration and Login System")
    print("A. Register\nB. Login\nC. Show Registered Users\nD. Exit")
    choice = input("Enter Your Choice A, B, C, D : ")
    if choice  == "A":
        username_inp = input("Enter Your Username : ").strip()
        password_inp = input("Enter Your Password : ").strip()
        for users in user:
            if username_inp == users['Username']:
                print("Username already exist! Try another Username")          
                break
                
        else:
            user.append({'Username':username_inp,'Password':password_inp})
            print("User Registered Sucessfully")
            

                
    elif choice == "B":
        username_inp = input("Enter Your Username : ").strip()
        password_inp = input("Enter Your Password : ").strip()
        
        for users in user:
            if username_inp == users['Username']:
                if password_inp == users['Password']:
                    print("Login Sucessfull")

                    while True:
                        print("A. Logout\nB. Back To Menu")
                        inputlogout = input("Enter Your Choice A, B : ")
                        if inputlogout == "A":
                            print("Log Out Sucessfully")
                            rerun = False
                            break
                        elif inputlogout == "B":
                            rerun = True
                            break
                        else:
                            print("Invalid Command")
                            False        
                else:
                    print("incorrect password")   
            else:
                print("username not found")
         
    elif choice == "C":
        print("Showing Registered Users")
        for users in user:
            print(f"Username:{users['Username']},Password:{users['Password']}")
            rerun = False
    elif choice == "D":
        print("Exit")
        rerun = False
    else:
        print("Invalid Command")
        




        
