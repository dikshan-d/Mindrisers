
# class Calculator:
#     def add(self,n1,n2):
#         return n1+n2
#     def sub(self,n1,n2):
#         return n1-n2
#     def mul(self,n1,n2):
#         return n1*n2
#     def div(self,n1,n2):
#         return n1/n2
# calculator = Calculator()
# while True:
#     while True:
#         try:
#             num1 = int(input("Enter the First Number:" ))
#             num2 = int(input("Enter the Second Number:" ))
#             break
        
#         except Exception as e:
#             print(e)
    
    
    
#     user_choose = input('choose command')
    
#     if user_choose == '+':
#         print("The Addition of",num1,"and",num2,"is", calculator.add(num1,num2))
#     elif user_choose == '-':
#         print("The Substraction of",num1,"and",num2,"is", calculator.sub(num1,num2))
#     elif user_choose == '*':
#         print("The Multiply of",num1,"and",num2,"is", calculator.mul(num1,num2))
#     elif user_choose == '/':
#         print("The Division of",num1,"and",num2,"is", calculator.div(num1,num2))
#         break
#     else:
#         print("Invalid Command")
    
   
import sys
import json

# Load existing products from file or initialize an empty list
try:
    with open("products.json", "r") as products_file:
        products = json.load(products_file)
except FileNotFoundError:
    products = []

cart = []

def save_cart_to_file():
    with open("cart.json", "w") as file:
        json.dump(cart, file)

def save_products_to_file():
    with open("products.json", "w") as products_file:
        json.dump(products, products_file)

def load_cart_from_file():
    try:
        with open("cart.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_products():
    print("Available Products:")
    for product in products:
        print(f"{product['id']}: {product['name']} - ${product['price']}")

def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append(product)
        save_cart_to_file()
        print(f"{product['name']} added to cart.")
    else:
        print("Product not found.")

def view_cart():
    total = sum(product["price"] for product in cart)
    print("Cart:")
    for product in cart:
        print(f"{product['name']} - ${product['price']}")
    print(f"Total: ${total}")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    new_id = 1 if not products else max(p["id"] for p in products) + 1
    new_product = {"id": new_id, "name": name, "price": price}
    products.append(new_product)
    save_products_to_file()
    print(f"Product '{name}' added with ID: {new_id}")

def remove_product():
    display_products()
    product_id = int(input("Enter the product ID to remove: "))
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        products.remove(product)
        save_products_to_file()
        print(f"Product '{product['name']}' (ID: {product_id}) removed.")
    else:
        print("Product not found.")

def main():
    global cart
    cart = load_cart_from_file()
    
    print("Welcome to CLI E-commerce!")
    
    while True:
        print("\nOptions:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Add Product")
        print("5. Remove Product")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_products()
        elif choice == "2":
            product_id = int(input("Enter product ID to add to cart: "))
            add_to_cart(product_id)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            add_product()
        elif choice == "5":
            remove_product()
        elif choice == "6":
            save_cart_to_file()
            print("Thank you for using CLI E-commerce!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






