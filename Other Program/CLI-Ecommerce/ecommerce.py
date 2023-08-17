import json
# products = []
cart = []
try:
    with open("Other Program/CLI-Ecommerce/products.json","r") as file:
        products = json.load(products,file)
except FileNotFoundError:
    products = []       
def save_product():
    with open("Other Program/CLI-Ecommerce/products.json","w") as file:

        json.dump(products,file)

def save_cart():
    with open("Other Program/CLI-Ecommerce/cart.json","w") as file:

        json.dump(cart,file)

def load_cart():
    try:
        with open("Other Program/CLI-Ecommerce/cart.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def display_product():
    print("Available Product")
    
    for product in products:
        print(f"{product['id']}: {product['name']} - {product['price']}")

def add_to_cart():
    pass
def view_cart():
    pass
def add_product():
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    newid = 1 if not products else max(p['id'] for p in products) + 1
    new_products = {"id": newid, "name":name, "price":price}
    products.append(new_products)
    save_product()
    print(f"Product {name}added with ID {newid}") #
def remove_product():
    pass
def main():
    global cart
    cart = load_cart()
    
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
            display_product()
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
            save_cart()
            print("Thank you for using CLI E-commerce!")
            exit()
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

