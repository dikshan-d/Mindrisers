#Implementing Global Variable, Function, Recursive Function and f string format


import time #importing time module
print("--------Timer Hai Yo Chai-------")
countdown = int(input("Timer Set Garnu : ")) #for global variable
def start_count():
    global countdown
    if countdown >= 4:
        print(f"Counting : {countdown}") #f String
        if countdown == 4:
            print("Time sakina lagyo hai")
        countdown -=1
        time.sleep(1) #for delaying 1 second
        start_count() #recursion

    
    elif countdown>0:
        print(f"Tik Tik : {countdown}")
        if countdown == 1:
            time.sleep(1)
            print("Launa Samaya Sakyo")
            exit()

        countdown -= 1
        time.sleep(1)
        start_count()
        
start_count()

