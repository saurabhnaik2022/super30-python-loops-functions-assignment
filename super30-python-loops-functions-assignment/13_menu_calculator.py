# Q13: Menu-Driven Calculator - WHILE loop keeps running until Exit
# Build a continuously running calculator using while. 
# Provide Addition, Subtraction, Multiplication, Division, Modulus, and Exit operations. 
# Handle division by zero properly.

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Modulus  6.Exit")
    choice = input("Choose: ")

    if choice == "6":
        print("Goodbye!")
        break
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice.")
        continue

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice in ("4", "5"):
        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", a / b if choice == "4" else a % b)
