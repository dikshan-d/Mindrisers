# def function(name,surname):
#     print(name,surname)
# name1 = input("N")
# surname2 = input("S")
# 
# function(name1,surname2)
# def sum(n1,n2):
#     add = n1+n2
#     print(add)
# num1 = int(input())
# num2 = int(input())
# add= sum(num1,num2)

# def naam(name):
#     print(name)
# a= 5
# b = 0
# while a>b:
#     name = input("Enter name")
#     b+=1
# naam(name)
#args
# def name(*naam,name1):
#     for i in naam:
#         print(i)
#     print(name1)
    
# name("Dikshan","Dangol",name1="d")
# name("hey","hi","hone",name1="Di")

#key word args
def naam(*nam,**name):
    # print(name.get("d"))
    print(name.keys())
    name1 = list(nam)
    name1[1]="Hello"

    # print(name1[1])
    return name
a = naam("hero","H",d="1",e="2")
print(a)