import faulthandler


products = []
def read_data():
   f = open("session08/test2.txt" , "r")
   for l in f:
        dic = {}
        result = l.split(",")
        dic = {"code": result[0], "name": result[1], "price" : result[2] , "count": result[3]}
        products.append(l)
        print(dic)


def add_product():
     code = input("enter code: ")
     name = input("enter name: ")
     price = input("enter price: ")
     count = input("enter count: ")
     dic ={"icode" : code , "name" : name , "price" : price , "count": count}
     products.append(dic)
     print(products)

def edit_product():
    code = input("Enter the product code: ")
    for product in data:
        if product['code'] == code:
            print("Which field do you want to edit?")
            print("1. Name")
            print("2. Price")
            print("3. Count")
            choice = int(input("Enter your choice: "))
        
            if choice == 1:
                new_name = input("Enter the new name: ")
                product['name'] = new_name
            elif choice == 2:
                new_price = float(input("Enter the new price: "))
                product['price'] = new_price
            elif choice == 3:
                new_count = int(input("Enter the new count: "))
                product['count'] = new_count
            else:
                print("Invalid choice!")
                return

            print("Product information has been updated successfully!")
            return

    print("Product not found!")

def remove_product():
    code = input("Enter the product code: ")
    for product in data:
        if product['code'] == code:
            data.remove(product)
            print("The desired product has been successfully removed!")
            return

    print("Product not found!")

def buy_product():
    cart = []
    while True:
        code = input("Enter the product code (leave empty to finish shopping): ")
        if code == "":
            break
        
        found = False
        for product in data:
            if product['code'] == code:
                found = True
                quantity = int(input("Enter the quantity you want to buy: "))
                
                if quantity > product['count']:
                    print("Not enough stock!")
                else:
                    cart.append({
                        'code': code,
                        'name': product['name'],
                        'price': product['price'],
                        'quantity': quantity})
                    product['count'] -= quantity
                    print(f"{product['name']} added to cart!")

                break

        if not found:
            print("Product not found!")

    total_price = 0
    print("\nInvoice:")
    print("-----------")
    for item in cart:
        subtotal = item['price'] * item['quantity']
        total_price += subtotal
        print(f"{item['name']} x {item['quantity']}: {subtotal} $")
        
    print("-----------")
    print(f"Total: {total_price} $")

data = read_data()

def save_data(data):
    with open('session08/test2.txt', 'w') as file:
        for product in data:
            line = f"{product['code']} , {product['name']} ,{product['price']} ,{product['count']}\n" 
            faulthandler.write(line)
        
def search_product():
    key = input("enter your key: ")
    for product in products:
        if key == product["id"] or key == product["name"]:
            print(product)
            break
    else:
        print("not found")

def show_products():
    print("code\t name \t price \t count")
    for product in products:
        print(product["code"] , "\t", product["name"], "\t" , product["price"], "\t", product["count"])

while True:
    print("\n========= Store =========")
    print("1. Add product")
    print("2. Search product")
    print("3. Edit product information")
    print("4. Remove product")
    print("5. Buy from the store")
    print("6. show products")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        search_product()
    elif choice == 3:
        edit_product()
    elif choice == 4:
        remove_product()
    elif choice == 5:
        buy_product()
    elif choice == 6:
        show_products()
    elif choice == 7:
        save_data(data)
        print("Data saved successfully. Exiting...")
        break
    else:
        print("Invalid choice!")

read_data()
