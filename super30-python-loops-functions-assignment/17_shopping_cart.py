# Q17: Shopping Cart - FUNCTIONS for each action; WHILE loop keeps the app running
# Create functions for add_item(), remove_item(), view_cart(), calculate_total(), and checkout(). 
# Keep the application running using a while loop until checkout or exit.

cart = []   # list of dictionaries: {"name", "price", "qty"}


def add_item(name, price, qty):
    for item in cart:
        if item["name"].lower() == name.lower():
            item["qty"] += qty
            print(f"Updated {name} quantity to {item['qty']}")
            return
    cart.append({"name": name, "price": price, "qty": qty})
    print(f"Added {name}")


def remove_item(name):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(f"Removed {name}")
            return
    print("Item not found.")


def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} - ₹{item['price']} x {item['qty']} = ₹{item['price'] * item['qty']}")


def calculate_total():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    return total


def checkout():
    if not cart:
        print("Cart is empty, nothing to checkout.")
        return False
    view_cart()
    print(f"Total payable: ₹{calculate_total()}")
    print("Thank you for shopping!")
    return True


while True:
    print("\n1.Add  2.Remove  3.View  4.Total  5.Checkout  6.Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_item(input("Item name: "), float(input("Price: ")), int(input("Quantity: ")))
    elif choice == "2":
        remove_item(input("Item name to remove: "))
    elif choice == "3":
        view_cart()
    elif choice == "4":
        print("Total: ₹", calculate_total())
    elif choice == "5":
        if checkout():
            break
    elif choice == "6":
        print("Exiting without checkout.")
        break
    else:
        print("Invalid choice.")
