# Q19: Bank Account - FUNCTIONS for each operation; WHILE loop keeps the app alive
# Create functions for deposit(), withdraw(), check_balance(), and transaction_history(). 
# Use a while loop to keep the banking application running. 
# Prevent withdrawals when sufficient balance is unavailable.

balance = 0
history = []   # list of transaction strings


def deposit(amount):
    global balance
    if amount <= 0:
        print("Amount must be positive.")
        return
    balance += amount
    history.append(f"Deposited ₹{amount}")
    print("Deposit successful.")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("Amount must be positive.")
    elif amount > balance:
        print("Insufficient balance! Withdrawal blocked.")
    else:
        balance -= amount
        history.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful.")


def check_balance():
    print(f"Current balance: ₹{balance}")


def transaction_history():
    if not history:
        print("No transactions yet.")
    for i, t in enumerate(history, 1):
        print(f"{i}. {t}")


while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.History  5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        deposit(float(input("Amount: ₹")))
    elif choice == "2":
        withdraw(float(input("Amount: ₹")))
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
