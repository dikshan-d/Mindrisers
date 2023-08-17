import random
while True:
    user = input("Choose Among Rock,Paper,Scissor : ")
    print("You Choose :",user)
    computer = random.choice(["Rock","Paper","Scissor"])
    print("Computer Choose :",computer)
    if user == computer:
        print("Draw")
    elif user == "Rock":
        if computer == "Paper":
            print("Your Lose")
        else:
            print("You Win")
    elif user == "Paper":
        if computer == "Scissor":
            print("Your Lose")
        else:
            print("You Win")
    elif user == "Scissor":
        if computer == "Rock":
            print("Your Lose")
        else:
            print("You Win")
    else:
        print("Invalid! Choose Among Rock, Paper, Scissor")
        continue      