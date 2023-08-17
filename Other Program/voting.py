# ask the user for their age
# if their age is above 18 or equal to 18 they can vote
#else if their age below 18 they cannot vote
# print("----------Voting System -------------")
# user_age = int(input("Enter Your Age: "))
# if (user_age == 18) or (user_age >= 18):
#     print("You can do Vote")
# else:
#     print("You cannot Vote")

def voting(votingage):
    if (votingage == 18) or (votingage >= 18):
        return print("You can do Vote")
    else:
       return print("You cannot Vote")


user_age = int(input("Enter Your Age: "))
age = voting(user_age)