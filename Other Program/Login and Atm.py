user = {'Ram':"123"}
def registration():
    print("Register Account")
    username = input("Enter Your Username : ")
    if username in user:
        return print("Username already Exist")
    password = input("Enter Your Password : ")
    user[username] = password
    print("Register Sucessfull")


def login():
    print("Login")
    username = input("Enter Your Username : ")
    if username not in user:
        return print("Username Incorrect")
    password = input("Enter Your Password : ")
    if user[username] == password:
        print("Login Sucessfull")
        atm()
    else:
        print("Incorrect Password")
debit_card = {}
def atm():
    while True:
        print("ATM")
        user_choice = input("Enter Your Choice\n1. Register\n2. Deposite\n3. Check Balance\n4. Go To Main Menu\nEnter choice here : ")
        if user_choice == "1":
            card_no = input("Enter Your debit card no : ")
            if card_no not in debit_card:
                debit_card[card_no]= 0
                print(card_no,"Registered")
            else:
                print("Debit card exist")
        elif user_choice == "2":
            card_no = input("Enter debit card : ")
            depo_amount = int(input("Enter the amount : "))
            if card_no in debit_card:
                debit_card[card_no] = debit_card[card_no]+depo_amount
                print(depo_amount,"Deposited")
            else:
                print("Debit card not exist")
        elif user_choice == "3":
            card_no= input("Enter debit card number : ")
            if card_no in debit_card:
                        print(f"Balance in the debit card {card_no}: {debit_card[card_no]}")
            else:
                print("Debit card does not exist.")
        elif user_choice == "4":
            main()
        else:
            print("Invalid Command")
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