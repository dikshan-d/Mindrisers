# list_fruits= ["Apple","Mango","Grape"]
# # c = 0
# for i in list_fruits:
#     # c+=1
#     print(")","First Letter of",i,"is :",i[0])
#     for j in i:
#         print(j)
# num = 9841008197

# for i in str(num):
#     print("--------------->\n--------------->\n======",i)

# list_fruits= ["Apple","Mango","Grape","Orange","Papaya"]
# for i in list_fruits:
#     if i not in ["Orange","Papaya","Mango"]:
#         print(i)
#Display directly
#Display with user input
a = True
while a:
    fruit_list = ["Mango","Papaya","Orange","Grape"]
    choose_menu = input("Choose A or B : ")
    if choose_menu == "A":
        for i in fruit_list:
            if i not in ["Mango"]:
                print(i)
    elif choose_menu == "B":
        exclude = input("Enter the ")
        storeexclude = exclude.split()
        for i in fruit_list:
            if i not in storeexclude:
                print(i)
    again = input("Enter: ")
    if again == "Y":
        a= True
    elif again == "N": 
        a=False
        
