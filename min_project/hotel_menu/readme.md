# Hotel Menu Ordering System

## Description
This is a simple Python program that simulates a menu ordering system for a hotel called **KHAJA HOUSE**. The program displays a predefined menu with prices, allows the user to place multiple orders, and calculates the total bill while ensuring case-insensitive input handling.

## Features
- Displays a menu with item names and prices.
- Takes user input to order an item (case-insensitive).
- Allows the user to place multiple orders in a loop.
- Computes and displays the total bill.
- Provides error handling for invalid menu items.

## Menu
 - Buff MO:MO        : Rs.160
 - Chicken MO:MO     : Rs.180
 - Veg MO:MO         : Rs.150
 - Veg ChauMin       : Rs.100
 - Buff ChauMin      : Rs.110
 - Thukpa            : Rs.280


## How It Works
1. The program welcomes the user and displays the menu.
2. The user is prompted to order an item from the menu.
3. The input is case-insensitive, meaning "buff mo:mo" and "BUFF MO:MO" are treated the same.
4. If the item exists in the menu, it is added to the total order.
5. The user is asked if they want to order another item.
6. If the user chooses to continue ordering, they can enter another item.
7. If the user enters an invalid item, they are prompted again.
8. Once the ordering process ends, the total bill is displayed.

## Requirements
- Python 3.x

## Running the Program
1. Save the script as **hotel_menu.py**.
2. Open a terminal or command prompt.
3. Run the script using:
   ```sh
   python hotel_menu.py
