import json
def display_product():
    f = open("Ecommerce.py/product.txt","r")
    a = f.read()
    productlist = a.split('-')
    for i in productlist:
        if i:
            aa = json.loads(i)
            product_id = list(aa.keys())[0]  # Get the product ID
            product_data = aa[product_id]
            print('product id:', product_id, 'name:', product_data[0], 'price:', product_data[1])

    f.close()
def display_cart():
   f = open("Ecommerce.py/cart.txt", "r")
   a = f.read()
   cart_list = a.split('-')
   total_price = 0  # Initialize the total price

   for i in cart_list:
        if i:
            item = json.loads(i)
            product_id = list(item.keys())[0]
            product_data = item[product_id]
            print('Product ID:', product_id, 'Name:', product_data[0], 'Price:', product_data[1])
            total_price += float(product_data[1])  # Add the price to the total

   print('Total Price:', total_price)  # Print the total price
   f.close()
   main()


    
def add_product():
    id = input("Enter the product id: ")
    product = input("Enter the product name: ")
    price = input("Enter the price id: ")
    f = open("Ecommerce.py/product.txt",'r')
    a = f.read()
    productlist = a.split('-')
    for i in productlist:
        if i != '':
            aa = json.loads(i)
            product_id = list(aa.keys())[0]  # Get the product ID
            product_data = aa[product_id]
            if  id in product_data:
                return print("id Exist")
            

    save = {id:[product,price]}
    f = open("Ecommerce.py/product.txt","a")
    f.write(json.dumps(save)+ "-")
    f.close()
    main()
def add_cart():
    id = input("Enter Product Id ")
    f = open("Ecommerce.py/product.txt","r")
    a = f.read()
    productlist = a.split('-')
    for i in productlist:
         if i != '':
            aa = json.loads(i)
            product_id = list(aa.keys())[0]  # Get the product ID
            product_data = aa[product_id]
            if id == product_id:
            
                print ("Product id",product_id,"added in cart")

                save = {product_id:[product_data[0],product_data[1]]}
                f = open("Ecommerce.py/cart.txt","a")
                f.write(json.dumps(save)+ "-")
                f.close()
                return
    print("id not found")
                
    main()
def remove_product():
    id = input("Enter the id ")
    f = open("Ecommerce.py/product.txt","r")
    a = f.read() 
    productlist = a.split('-')
    for i in productlist:
        aa = json.loads(i)
        product_id = list(aa.keys())[0]  # Get the product ID
        product_data = aa[product_id]
        if id == product_id:
           product_data.remove(product_data)

    
           

def main():
    while True:
        user_choice = input("Choice")
        if user_choice == "ap":
            add_product()
        elif user_choice =="dp":
            display_product()
        elif user_choice == "ac":
            add_cart()
        elif user_choice =='dc':
            display_cart()
        elif user_choice =='r':
            remove_product()
main()