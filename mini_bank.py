def see_bank_account_balance():
    print(f"Your current bank account balance is: ${balance:.2f}")

def deposit_money():
    global balance
    amount =  int(input("Enter the amount to deposit: "))
    balance = amount + balance

def pull_money():
    global balance
    pull_amount = int(input("Enter the amount to withdraw: "))
    if pull_amount > balance:
        print("Insufficient funds.")
    else:
        balance -= pull_amount
        print(f"${pull_amount} has been withdrawn. New balance: ${balance:.2f}")

def exit_program():
    print("Exiting the program. Goodbye!\n")
    exit()

balance = float(100.00)  # Initial balance

print("Welcome to the Mini Bank!\n1.See Bank Account Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")

while True:
    user_input = input("Please select an option (1-4): ")

    if user_input == "1":
        see_bank_account_balance()

    elif user_input == "2":
        deposit_money() 

    elif user_input == "3":
        pull_money()

    elif user_input == "4":
        exit_program()

    else:
        print("Invalid option selected. Please try again.")
        exit_program()
