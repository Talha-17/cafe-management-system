# Define the menu of the restaurant

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

# Greet the customer
print("Welcome To Python Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

# Initialize total bill
order_total = 0

# First order
item_1 = input("\nEnter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available.")

# Ask for another item
another_order = input("\nDo you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available.")

# Display total bill
print(f"\nThe total amount to pay is Rs{order_total}")