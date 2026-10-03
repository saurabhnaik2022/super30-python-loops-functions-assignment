# Q10: ATM Simulator - WHILE loop because we don't know how many transactions the user will do
# Start with a balance of ₹10,000. 
# Continuously show the user options to check balance, deposit money, withdraw money, or exit. 
# The program should continue until the user explicitly chooses Exit.

balance = 10000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Balance: ₹{balance}")
    elif choice == "2":
        amount = float(input("Deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print("Deposited. New balance:", balance)
        else:
            print("Enter a positive amount.")
    elif choice == "3":
        amount = float(input("Withdraw amount: ₹"))
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawn. New balance:", balance)
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option.")
