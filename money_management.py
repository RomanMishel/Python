
def add_purchase(purchases):
    purchase_name = input("Enter the name of the purchase: ")
    purchase_price = input("How much did it cost: ")

    if not purchase_price.replace('.', '', 1).isdigit():
        print("Please enter a valid price.\n")
        return

    purchases.append({"name": purchase_name, "price": float(purchase_price)})

    print("Purchase added!\n")
    return

def view_purchases(purchases):
    if len(purchases) == 0:
        print("No purchases yet.")
        return

    total_cost = 0
    for index, purchase in enumerate(purchases, start=1):
        print(f"{index}. {purchase['name']} - ${purchase['price']:.2f}\n")
        total_cost += purchase['price']

    print(f"Total cost: ${total_cost:.2f}\n")

def reset_purchases(purchases):
    purchases.clear()
    print("Purchases list was cleared.\n")

def exit_program():
    print("Exiting the program. Goodbye!\n")
    exit()

purchases = []

while True:
    print("1.Add a purchase\n2.View purchases list\n3.Reset a purchase list\n4.Exit")
    user_input = input("Choose an option: ")
  
    if user_input == "1":
        add_purchase(purchases)
    elif user_input == "2":
        view_purchases(purchases)
    elif user_input == "3":
        reset_purchases(purchases)
    elif user_input == "4":
        exit_program() 
    else:
        print("Invalid option. Please choose a valid option.")
        exit_program()
