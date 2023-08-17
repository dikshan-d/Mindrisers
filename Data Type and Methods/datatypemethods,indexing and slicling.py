user_choose = input("Choose A or B: ")
if user_choose=="A":                                                          
    #String Methods
    #for converting lower word into upper and upper word into lower
    input = input("Enter the word: ")
    if input == input.lower():
        print(input,"is lower word\nconverting",input,"into upper word :",input.upper())
    elif input == input.upper():
        print(input,"is upper word\nconverting",input,"into lower word :",input.lower())

    #for converting word into capatilize 
    print("capatilizing",input,":",input.capitalize())
elif user_choose == "B":
    #List Method
    input_list = input("Enter the List: ")
    List = input_list.split()
    print(List)
    method = ''.join(List).count("h")
    print(method)
