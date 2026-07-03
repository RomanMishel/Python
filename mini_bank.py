def see_bank_account_balance():
    print(f"Your current bank account balance is: ${balance:.2f}")

def deposit_money():
    amount =  input("Enter the amount to deposit: ")
    amount = amount + balance 

def pull_money():
    pull_amount = input("Enter the amount to withdraw: ")
    if pull_amount > balance:
        print("Insufficient funds.")
    else:
        balance -= pull_amount
        print(f"${pull_amount} has been withdrawn. New balance: ${balance:.2f}")

def exit_program():
    print("Exiting the program. Goodbye!\n")
    exit()

balance = float(100.00)  # Initial balance

