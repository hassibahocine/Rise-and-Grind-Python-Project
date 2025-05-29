# Write Functions here
import json

def write(data, jsonfile = "JSON/Stock.json"):#Makes changes to the dictionary (defaulted as the Stock json file)
    jsonread = dict(read(jsonfile))
    jsonread = data
    jsonwrite(jsonread, jsonfile)

def jsonwrite(data, jsonfile = "JSON/Stock.json"):#Used by the write function, used to dump the input dictionary into a json file (default stock)
    with open (jsonfile, "w") as Stock:
        json.dump(data, Stock, indent = 4)

def read(jsonfile = "JSON/Stock.json"):#Returns the dictionary of a file, defaults to stock
    with open (jsonfile, "r") as Stock:
        return(json.load(Stock))

def bookwrite():#Asks for book info from user, adds it to the stock json file
    name = input("Name of book: ")
    while True:
        price = input("Price of book: ")
        try:
            float(price)
            break
        except:
            print("Invalid Input")
    author = input("Author of book: ")
    details = input("Details of book: ")
    while True:
        stock = input("How much stock: ")
        try:
            int(stock)
            break
        except:
            print("Invalid Statement")

    jsonfile = dict(read())
    jsonfile["Book"][name.title()] = {
        "Price" : price,
        "Author" : author,
        "Details" : details,
        "Stock" : stock
    }

    write(jsonfile)

def foodwrite():#same as bookwrite(), asks for user input and puts a new food into stock.json
    name = input("Name of Food: ")
    while True:
        price = input("Price of Food: ")
        try:
            float(price)
            break
        except:
            print("Invalid Input")
    allergens = input("Allergens: ")
    details = input("Details of Food: ")
    while True:
        stock = input("How much stock: ")
        try:
            (int(stock))
            break
        except:
            print("Invalid Input")
            
    jsonfile = dict(read())
    jsonfile["Food"][name.title()] = {
        "Price" : price,
        "Allergens" : allergens,
        "Details" : details,
    }

    write(jsonfile)


def drinkwrite():#same as bookwrite(), asks for user input and puts a new drink into stock.json
    name = input("Name of Drink: ")
    while True:
        price = input("Price of Drink: ")
        try:
            float(price)
            break
        except:
            print("Invalid Input")
    allergens = input("Allergens: ")
    details = input("Details of Drink: ")
    
    while True:
        stock = input("How much stock: ")
        try:
            (int(stock))
            break
        except:
            print("Invalid Input")
    jsonfile = dict(read())
    jsonfile["Drink"][name.title()] = {
        "Price" : price,
        "Allergens" : allergens,
        "Details" : details,
        "Stock" : stock
    }
    write(jsonfile)

def show_item(item_name, item_type):#Returns the info of a certain item (in dictionary form)
    stock = read()
    return stock[item_type][item_name]

def rem_stock(item_name, item_type):#Deletes an item from the stock json
    stock = read()
    del(stock[item_type][item_name])
    jsonwrite(stock)

def discount_add(item_name, item_type, dic_val):#adds a discount for an item in discount json file
    discounts = read("JSON/Discounts.json")
    discounts[item_type][item_name] = dic_val
    jsonwrite(discounts, "JSON/Discounts.json")

def discount_rem(item_name, item_type):#Removes a discount for an item in the discount json file
    discounts = read("JSON/Discounts.json")
    del(discounts[item_type][item_name])
    jsonwrite(discounts, "JSON/Discounts.json")

def discount_list(item_type): #Returns all active discounts (present in 'Discounts.json') of a given item type
    discounts = read("JSON/Discounts.json")
    type_discounts = discounts[item_type]
    return type_discounts

def discount_apply(item_type, item_name):
    stock = read("JSON/Stock.json")
    discounts = discount_list(item_type)
    if item_name in discounts:
        normal = stock[item_type][item_name]["Price"]
        changed = discounts[item_name]
        newprice = normal * (changed / 100)
        return newprice
    else:
        return stock[item_type][item_name]["Price"]

#This is the old one, kept just in case new is bad
# def employeelogin():#Asks for user login and checks if it is the only employee allowed in the back of the system
#     username = input("Username: ").lower()
#     password = input("Password: ")
#     usr = "employee1".lower()
#     psw = "password123"
#     if username == usr and password == psw:
#         return True
#     else:
#         return False

def employeelogin():#Ask for username and password, return if in system
    usr = []
    psw = []
    emp = read("JSON/employees.json")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        try:
            if emp[username] == password:
                return True
            else:
                print("Invalid Password")
        except:
            print("Invalid username")
        if str.lower(input("Would you like to try again? Y/N\n")) == "n":
            return False

def add_employee():#ask user+pass then add to employees json file
    emp_dic = read("JSON/employees.json")
    username = input("What is the username?\n")
    password = input("What would you like your password to be?\n")
    emp_dic[username] = password
    jsonwrite(emp_dic, "JSON/employees.json")

def employee_rem():#Removes a discount for an item in the discount json file
    emp_dic = read("JSON/employees.json")
    del(emp_dic[input("Which employee do you wish to delete?\n")])
    jsonwrite(emp_dic, "JSON/employees.json")

def delivery_option():#Asks for name, checks if they already exist and if not to add their info
    customer = dict(read("JSON/Customers.json"))
    name = input('Whats your name? ')
    if name in customer["Customers"]:
        return print('Your details are aready saved')
    address = input('Whats your address? ')
    postcode = input('Whats your postcode? ')
    customer["Customers"][name.title()] = {
        "address" : address,
        "postcode" : postcode
    }
    jsonwrite(customer,'JSON/customers.json')
    return print('Thank you for your details')
    
def order():#Allows customer to add items from all 3 catagories and complete an order, printing total price
    stock = read()
    order = []
    total = 0.0
    while True:
            print("\nWhat would you like to order?")
            
            category = input("1. Food\n2. Drink\n3. Book\n4. Finish Order\n5. Quit\n")
            try:
                int(category)
            except:
                print("invalid input")
                continue
            if category == "1":
                for item, details in stock["Food"].items():
                    if details["Stock"] > 0:
                        print(f"{item}\t\t\t£{details['Price']}")

                selected_item = input("Select a food item: ").title()
                if selected_item in stock["Food"]:
                    quantity = int(input(f"How many {selected_item}s would you like to order? "))
                    if stock["Food"][selected_item]["Stock"] >= quantity:
                        #order.append((selected_item, quantity, stock["Food"][selected_item]["Price"]))
                        order.append((selected_item, quantity, discount_apply("Food", selected_item)))
                        total += discount_apply("Food", selected_item) * quantity
                        #total += stock["Food"][selected_item]["Price"] * quantity
                        print(f"{quantity} {selected_item}(s) added to your order.")
                    else:
                        print("Sorry, not enough stock available.")
                else:
                    print("Invalid food item.")
                
            elif category == "2":
                for item, details in stock["Drink"].items():
                    if details["Stock"] > 0:
                        print(f"{item}\t\t\t£{details['Price']}")

                selected_item = input("Select a drink item: ").title()
                if selected_item in stock["Drink"]:
                    quantity = int(input(f"How many {selected_item}s would you like to order? "))
                    if stock["Drink"][selected_item]["Stock"] >= quantity:
                        #order.append((selected_item, quantity, stock["Drink"][selected_item]["Price"]))
                        order.append((selected_item, quantity, discount_apply("Drink", selected_item)))
                        total += discount_apply("Drink", selected_item) * quantity
                        #total += stock["Drink"][selected_item]["Price"] * quantity
                        print(f"{quantity} {selected_item}(s) added to your order.")
                    else:
                        print("Sorry, not enough stock available.")
                else:
                    print("Invalid drink item.")
                
            elif category == "3":
                for item, details in stock["Book"].items():
                    if details["Stock"] > 0:
                        print(f"{item}\t\t\t£{details['Price']}\nAuthor: {details['Author']}")

                selected_item = input("Select a book item: ").title()
                if selected_item in stock["Book"]:
                    quantity = int(input(f"How many {selected_item}s would you like to order? "))
                    if stock["Book"][selected_item]["Stock"] >= quantity:
                        order.append((selected_item, quantity, discount_apply("Book", selected_item)))
                        total += discount_apply("Book", selected_item) * quantity
                        #order.append((selected_item, quantity, stock["Book"][selected_item]["Price"]))
                        #total += stock["Book"][selected_item]["Price"] * quantity
                        print(f"{quantity} {selected_item}(s) added to your order.")
                    else:
                        print("Sorry, not enough stock available.")
                else:
                    print("Invalid book item.")
                
            elif category == "4":
                print("\nOrder Summary:\n")
                for item, quantity, price in order:
                    print(f"{item} x{quantity} = £{price * quantity:.2f}\n")
                total = sum(price * quantity for item, quantity, price in order)
                print(f"\nTotal: £{total:.2f}")
                while True:   
                    confirm = input("Confirm?\n1. Yes\n2. No \n")
                    if confirm.lower() == '1':
                        print("Your order has been placed!")
                        break
                    elif confirm == "2":
                        print("Order cancelled. You can add more items.")
                        break
                    else: print("Invalid input")
                
            elif category == "5":
                print("Quit")
                break
            else:
                print("Invalid Input")

def viewcustomerRecords():
    customers = read('JSON/Customers.json')
    for name in customers["Customers"]:
        print(f"{name}\nAddress: {customers["Customers"][name]["address"]}\nPostcode: {customers["Customers"][name]["postcode"]}\n")