import bankdata
import functions
import helper

account = functions.login(bankdata.accounts)
while account is None:
    account = functions.login(bankdata.accounts)

while True:
    print("\n--------------------------------")
    print(f"Logged in as: {account['name']}")
    print("--------------------------------")
    print("1. View balance of your account: ")
    print("2. Withdraw money from your account: ")
    print("3. Deposit money to your account: ")
    print("4. View statement of your account: ")
    print("5. Switch account")
    print("6. Exit")
    print()

    choice = helper.int_error("Enter your choice: ")

    if choice == 1:
        functions.balance(account)
    elif choice == 2:
        amount = helper.amount_error("Enter the amount to withdraw: ")
        functions.withdraw(account, amount)
    elif choice == 3:
        amount = helper.amount_error("Enter the amount you want to deposit: ")
        functions.deposit(account, amount)
    elif choice == 4:
        functions.statement(account)
    elif choice == 5:
        account = functions.login(bankdata.accounts)
        while account is None:
            account = functions.login(bankdata.accounts)
    elif choice == 6:
        print("Thank you for using our banking system. Goodbye!")
        break
