
items = []
prices = []

def menu():
    print("\nWelcome to the Shopping Cart Program!\n")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View the cart")
    print("3. Remove an item")
    print("4. Compute the total")
    print("5. Quit")

def add_item():
    item = input("\nWhat item would you like to add? ")
    price = float(input("What is the price of '{}'? $".format(item)))
    items.append(item)
    prices.append(price)
    print("'{}' has been added to the cart.\n".format(item))

def view_cart():
    if not items:
        print("\nThe cart is empty.\n")
    else:
        print("\nThe contents of the shopping cart are:\n")
        for i in range(len(items)):
            print("{}. {} - ${:.2f}".format(i+1, items[i], prices[i]))
        print("")

def remove_item():
    if not items:
        print("\nThe cart is empty.\n")
        return
    view_cart()
    index = int(input("Which item would you like to remove? "))
    if index < 1 or index > len(items):
        print("\nInvalid choice. Please select a number between 1 and {}\n".format(len(items)))
        return
    item = items.pop(index-1)
    price = prices.pop(index-1)
    print("'{}' has been removed from the cart.\n".format(item))

def compute_total():
    if not items:
        print("\nThe cart is empty.\n")
        return
    total = sum(prices)
    print("\nThe total price of the items in the cart is ${:.2f}\n".format(total))

while True:
    menu()
    choice = input("Please enter an action: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        compute_total()
    elif choice == '5':
        print("Thank you.\nGoodbye.")
        break
    else:
        print("\nInvalid choice. Please select a number between 1 and 5\n")