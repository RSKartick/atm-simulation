import json
import datetime
import helper

#Display Balance
def balance(account):
    print("Your balance is: ", f"{account['balance']}")
    print("\n")

# - Deposit Money
def deposit(account, amount):
    if amount <= 0:
        print("Invalid Amount.")
    else:
        account["balance"] += amount
        account["transactions"].append(f"+{amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{amount} credited to your account")

# - Withdraw Money
def withdraw(account, amount):
    if amount <= 0:
        print("Invalid Amount.")
        return
    elif amount > account["balance"]:
        print("Insufficient balance")
        return
    account["balance"] -= amount
    account["transactions"].append(f"-{amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{amount} debited from your account")

# - Statement (transaction record)
def statement(account):
    print("Your transaction record is: ")
    for transaction in account['transactions']:
        print(f"{transaction.strip()}")

# - Login
def login(accounts):
    account_no = helper.int_error("Enter account number: ")
    if account_no not in accounts:
        print("Account not found.")
        return None
    pin = helper.int_error("Enter PIN: ")
    if accounts[account_no]["pin"] != pin:
        print("Incorrect PIN.")
        return None
    print(f"Welcome, {accounts[account_no]['name']}!")
    return accounts[account_no]
