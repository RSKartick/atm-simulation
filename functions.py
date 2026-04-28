import datetime

#Display Balance
def balance(account):
    print("Your balance is: ", f"{account['balance']}")
    print("\n")

# - Withdraw Money
def deposit(account, amount):
    account["balance"] += amount
    account["transactions"].append(f"+{amount}")
    print(f"{amount} credited to your account")

# - Deposit Money
def withdraw(account, amount):
    if amount > account["balance"]:
        print("Insufficient balance")
        return
    
    account["balance"] -= amount
    account["transactions"].append(f"-{amount}")
    print(f"{amount} debited from your account")

# - Statement (transaction record)
def statement(account):
    print("Your transaction record is: ")
    for transaction in account['transactions']:
        print(f"{transaction.strip()} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# - Login
def login(accounts):
    account_no = int(input("Enter account number: "))
    if account_no not in accounts:
        print("Account not found.")
        return None
    pin = int(input("Enter PIN: "))
    if accounts[account_no]["pin"] != pin:
        print("Incorrect PIN.")
        return None
    print(f"Welcome, {accounts[account_no]['name']}!")
    return accounts[account_no]
