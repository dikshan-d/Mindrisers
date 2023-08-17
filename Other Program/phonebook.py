# empty name, phonenumber, and how many user detail number you save 
#name and phone number input inside for loop with numver of user detaiil and use append to save that input in empty variable
# print the name and phone number'
# inside for loop print in tabular format with index name and phone number
# searching input and print searching
# use if condition if searching found in name . use saved name variable.index and searching in parethesis
#phone number with index in list
# and print in format and tabformat {},{}".format()
#else not found
a= True
while a:
    names = []
    phonenumbers = []
    num = 2

    for i in range(num):
        name = input("Enter Your Full Name: ")
        phonenumber = input("Enter Your Phone Number: ")
        
        names.append(name)
        phonenumbers.append(phonenumber)

    print("Names\t\t|\tPhonenumbers")
    for i in range(num):
        print("{}\t\t|\t{}".format(names[i],phonenumbers[i]))

    search = input("Enter Your Name For Viewing Your Contact Details : ")
    print(search,"Your Contact Detail:")
    if search in names:
        index = names.index(search)
        contact = phonenumbers[index]
        print("Name {} PhoneNumber {}".format(search,contact))
    else:
        print("Contact Not Found")
    uc = input("ENter")
    if uc == "1":
        searchforedit = input("Enter the name")
        if searchforedit in names:
            newname= input("Enter")
            index1 = names.index(searchforedit)
            names[index] = newname

    for i in range(num):
        print("{}\t\t|\t{}".format(names[i],phonenumbers[i]))     
    p = input("Enter")
    if p =="+":
        a = True
    else:
        a = False