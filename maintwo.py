lst = {}
class Bank:
    def __init__(self,account,own):
        self.account = account
        self.own = own


def show(user):
    print("Current Balance:", lst[user].own)
def deposit(user):
    depo = int(input("Enter deposit amount: "))
    if depo > 0:
        lst[user].own += depo
        print("Deposit completed successfully.")
    elif depo == 0:
        print("Deposit amount must be greater than zero.")
    else:
        print("Deposit amount cannot be negative.")
    
def withdraw(user):
    withdraw_amount = int(input("Enter withdrawal amount: "))
    if withdraw_amount > lst[user].own:
        print("Insufficient balance.")
    elif withdraw_amount < 0:
        print("Withdrawal amount cannot be negative.")
    else:
        lst[user].own -= withdraw_amount
        print("Withdrawal completed successfully.")
def action(acount):
    command = input("Select an operation: ")
    if command == "show" or command == "Show":
        show(acount)
    elif command == "deposit" or command == "Deposit":
        deposit(acount)
    elif command == "Withdraw" or command == "withdraw":
        withdraw(acount)
    else:
        print("Invalid selection.")

def initial():
    stat = input("Do you have an existing account? (yes/no): ")
    account_exist(stat)
    
def account_exist(var):
    if var == "yes" or var == "Yes":
        accountt = input("Enter account name: ")
        if accountt not in lst:
            print("Account not found.")
        else:
            action(accountt)
    elif var == "no" or var == "NO" or var == "No":
        print("Create an account to get started.")
        new_user = input("Enter account name: ")
        while new_user == "" or new_user in lst:
            if new_user == "":
                print("Invalid account name.")
                account_exist(var)
        
            elif new_user in lst:
                print("An account with this name already exists.")
                print("Please choose a different account name.")
                account_exist(var)
        lst[new_user] = Bank(new_user,0)
        print("Account created successfully.")
    else:
        print("Invalid input.")

while True:
    initial()
