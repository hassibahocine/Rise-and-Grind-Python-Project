import Functions as f
while True:
    print("\nWelcome to Rise and Grind!\n"
        "Please select an option:\n"
        "1. View Menu\n"
        "2. Place an Order\n"
        "3. Return/Refund\n"
        "4. Employee Login\n"
        "5. Exit\n")

    option = input("\nPlease select an option: ")
    if option == "1":#View menu
        while True:
            stock = f.read()
            match input("Which would you like to view?\n1. Food\n2. Drink\n3. Book\n4. Quit\n"):
                case "1":
                    for item in stock["Food"]:
                        if stock["Food"][item]["Stock"] >0:
                            print(f"{item}\t\t\t£{stock["Food"][item]["Price"]}\nAllergens: {stock["Food"][item]["Allergens"]}\n{stock["Food"][item]["Details"]}\n")
       
                case "2":
                    for item in stock["Drink"]:
                        if stock["Drink"][item]["Stock"] >0:
                            print(f"{item}\t\t\t£{stock["Drink"][item]["Price"]}\nAllergens: {stock["Drink"][item]["Allergens"]}\n{stock["Drink"][item]["Details"]}\n")
                    input("Next item")
                case "3":
                    for item in stock["Book"]:
                        if stock["Book"][item]["Stock"] >0:
                            print(f"{item}\t\t\t£{stock["Book"][item]["Price"]}\nAuthor: {stock["Book"][item]["Author"]}\n{stock["Book"][item]["Details"]}\n")
                    input("Next item")
                case "4":
                    break
                case _:
                    print("Invalid Input")
    elif option == "2":#Place an order
        while True:
            delivery = input('1. Eat in\n2. Delivery\n3. Quit\n')
            if delivery.lower() == '1':
                f.delivery_option()
                f.order()
            elif delivery.lower() == '2':
                f.order()
            elif delivery == "3":
                break
            else:
                print("Invalid Input")
               
    elif option == "3":
        while True:
            print("Please choose from the following options:\n")
            choice = input("1. Return/Refund \n2. Contact Customer Support \n3. Quit \n")
            if choice == "1":
                print("Please contact Sheila on 03005557437 for your refund request!")
            elif choice == "2":
                print("Sorry to hear you are having issues, please contact our customer support team on 03005547463 and they will be more than happy to help!")
            else:
                break
    
    elif option == "4":#Employee login
        while True:
            if f.employeelogin():
                while True:
                    option = input("\n1. Add Stock\n"
                                "2. Remove stock\n"
                                "3. Add Discount\n"
                                "4. Remove Discount\n"
                                "5. Manage Employees\n"
                                "6. View Customer Records\n"
                                "7. Quit\n")
                    
                    if option == "1":
                        while True:
                            option = input("\nAdd:"
                                        "\n1. Food\n"
                                        "2. Drink\n" 
                                        "3. Book\n"
                                        "4. Manage Employees"
                                        "5. Quit\n")
                            
                            if option == "1":
                                f.foodwrite()
                            elif option == "2":
                                f.drinkwrite()
                            elif option == "3":
                                f.bookwrite()
                            elif option == "4":
                                break
                            else:
                                print("Invalid Input")
                    elif option == "2":
                        while True:

                            option = input("\nRemove: \n" \
                            "1. Food\n" \
                            "2. Drink\n" \
                            "3. Book\n" \
                            "4. Quit\n")

                            if option == "1":
                                stock = input("What do you want to remove?: ").title()
                                if stock in f.read()["Food"]:
                                    f.rem_stock(stock, "Food")
                                else:
                                    print("Invalid Option")

                            elif option == "2":
                                stock = input("What do you want to remove?: ").title()
                                if stock in f.read()["Drink"]:
                                    f.rem_stock(stock, "Drink")
                                else:
                                    print("Invalid Option")

                            elif option == "3":
                                stock = input("What do you want to remove?: ").title()
                                if stock in f.read()["Book"]:
                                    f.rem_stock(stock, "Book")
                                else:
                                    print("Invalid Option")

                            elif option == "4":
                                break
                    elif option == "3":
                        while True:
                            item_type = input("Would you like to add a discount for: \n" \
                            "1. Food\n" \
                            "2. Drink\n" \
                            "3. Book\n" \
                            "4. Quit\n")
                            if item_type == "4":
                                break
                            elif item_type == "1":
                                item_type = "Food"
                            elif item_type == "2":
                                item_type = "Drink"
                            elif item_type == "3":
                                item_type = "Book"
                            item_name = input("What's the name of the item?:\n")
                            if item_name.title() == "Quit":
                                break
                            else:
                                while(True):
                                    discount = input("How much of a discount?\n")
                                    if discount.isnumeric():
                                        f.discount_add(item_name.title(), item_type.title(), int(discount))
                                        break
                                    else:
                                        print("Invalid Input")
                    elif option == "4":
                        while True:
                            print("These are all the discounts in effect:\n")
                            print("\n------------------------------------\n")
                            for discount, discount_val in f.discount_list("Book").items():
                                print(f"Book: {discount} with a {discount_val}% discount")
                            for discount, discount_val in f.discount_list("Food").items():
                                print(f"Food: {discount} with a {discount_val}% discount")
                            for discount, discount_val in f.discount_list("Drink").items():
                                print(f"Drink: {discount} with a {discount_val}% discount")
                            print("\n------------------------------------\n")
                            discount_to_del = input(
                                "\nEnter the type of discount to remove: \n" \
                                "1. Books\n" \
                                "2. Food\n" \
                                "3. Drink\n" \
                                "4. Quit\n"
                                )
                            if discount_to_del == "1":
                                discount_del_type = "Book"
                            elif discount_to_del == "2":
                                discount_del_type = "Food"
                            elif discount_to_del == "3":
                                discount_del_type = "Drink"
                            elif discount_to_del == "4":
                                break
                            else:
                                print("\nThat wasn't one of the options, try again\n")
                                continue
                            discount_name = input("Please write discount item name\n")
                            if discount_name.title() in f.discount_list(discount_del_type):
                                f.discount_rem(discount_name.title(), discount_del_type)
                                print(f"\n{discount_name} discount removed \n")
                            else:
                                print("There wasn't anything with that name, of that type, try again")
                                continue
                    elif option == "5":
                        while True:
                            emp = f.read("JSON/employees.json")
                            match input("What would you like to do?\n"
                                    "1. View Employees\n"
                                    "2. Add Employee\n"
                                    "3. Remove Employee\n"
                                    "4. Quit\n"):
                                case"1":
                                    print("Employees\n")
                                    emp = {key: value for key, value in sorted(emp.items())}
                                    for i in emp:
                                        print(i)
                                    input("Press enter")
                                case"2":
                                    f.add_employee()
                                case"3":
                                    f.employee_rem()
                                case"4":
                                    break

                    elif option == "6":
                        f.viewcustomerRecords()
                    elif option == "7":
                        break
                    else:
                        print("Invalid Input")
                if str.lower(input("Would you like to login with another user? Y/N\n")) =="y":
                    continue
                else:
                    break
            else:
                break
    elif option == "5":
        print("Thank you for visiting Rise and Grind!")
        break
    
    else:
        print("Invalid Input")
 