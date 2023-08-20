# while True:
#     a = int(input("Enter the first number : "))
#     b = int(input("Enter the second number : "))

#     if (a>b):
#         print("a is greater than b")
        

#     elif (a<b):
#         print("b is greater than a")
#         break
#     else:
#             print("Number is Equal")

def greatest(a,b,c):
    if (a>b) and (a>c):
       return print("a is greater than b and c")
        
    elif (b>c) and (b>a):
       return print("b is greater than a and c")
    elif (c>b) and (c>b):
       return print("c is greater than a and b")
    else:
       return print("All Number are Equal, Do Again")
while True: # For rerunning the code
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    c = int(input("Enter the third number : "))
    Max = greatest(a,b,c)
