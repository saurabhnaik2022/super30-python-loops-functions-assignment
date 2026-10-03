# Q11: Password Retry - WHILE loop with an attempt counter (max 3)
# Store a predefined password and give the user a maximum of three attempts to enter it correctly. 
# Use a while loop. 
# After three incorrect attempts, display "Account Locked".
PASSWORD = "super30@123"
attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    entered = input("Enter password: ")
    if entered == PASSWORD:
        print("Access Granted!")
        break
    attempts += 1
    print(f"Wrong password. Attempts left: {MAX_ATTEMPTS - attempts}")
else:
    # runs only if the loop finished without 'break'
    print("Account Locked")
