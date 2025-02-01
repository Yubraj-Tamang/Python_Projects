# Define the menu of the hotel
menu = {
    "Buff MO:MO": 160,
    "Chicken MO:MO": 180,
    "Veg MO:MO": 150,
    "Veg ChauMin": 100,
    "Buff Chaumin": 110,
    "Thukpa": 280
}

# Create a case-insensitive menu lookup dictionary
menu_lower = {item.lower(): price for item, price in menu.items()}

# Greeting customer
print("----Welcome to KHAJA HOUSE----")
print("Here's our menu:")
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

# Total bill
total_order = 0

# Loop to take orders
while True:
    user_order = input("\nOrder an item from the menu: ").strip().lower()
    
    if user_order in menu_lower:
        total_order += menu_lower[user_order]
        # Find the original formatted name for display
        original_name = [name for name in menu if name.lower() == user_order][0]
        print(f"Your order is placed: {original_name}")
    else:
        print("Sorry, that item is not on the menu. Please order again.")
        continue  # Ask again instead of moving forward

    another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another_order != "yes":
        break  # Exit loop if the user does not want another item

# Display the final bill
print(f"\nYour total bill is Rs.{total_order}. Thank you for visiting KHAJA HOUSE!")
