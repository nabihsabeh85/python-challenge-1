# Menu dictionary
menu ={
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

    # ... (include your full menu dictionary here as you provided earlier)

def print_menu_category(menu, category_name):
    """
    Function to print the items in a specific menu category.
    """
    print(f"What {category_name} item would you like to order?")
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in menu[category_name].items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                item_name = f"{key} - {sub_key}"
                print(f"{i:6} | {item_name:24} | ${sub_value}")
                menu_items[i] = {"Item name": item_name, "Price": sub_value}
                i += 1
        else:
            print(f"{i:6} | {key:24} | ${value}")
            menu_items[i] = {"Item name": key, "Price": value}
            i += 1
    return menu_items

def main():
    # Launch the store and present a greeting to the customer
    print("Welcome to the variety food truck.")

    # Initialize the order list
    orders = []

    place_order = True
    while place_order:
        # Print menu categories
        print("From which menu would you like to order? ")
        menu_items = {}
        i = 1
        for key in menu.keys():
            print(f"{i}: {key}")
            menu_items[i] = key
            i += 1

        # Get the customer's menu category input
        menu_category = input("Type menu number: ")
        if menu_category.isdigit() and int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            # Print the selected menu category and get the item selection
            category_menu_items = print_menu_category(menu, menu_category_name)
            item_selection = input("Type item number: ")

            if item_selection.isdigit() and int(item_selection) in category_menu_items.keys():
                selected_item = category_menu_items[int(item_selection)]
                item_name = selected_item["Item name"]
                price = selected_item["Price"]

                # Get the quantity
                quantity_input = input(f"How many of '{item_name}' would you like? (Default is 1): ")
                quantity = int(quantity_input) if quantity_input.isdigit() else 1

                # Add to order list
                orders.append({"Item name": item_name, "Price": price, "Quantity": quantity})
            else:
                print("Invalid item selection.")

        else:
            print(f"{menu_category} is not a valid menu option.")

        # Check if the customer wants to keep ordering
        while True:
            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
            if keep_ordering == 'n':
                print("Thank you for your order.")
                place_order = False
                break
            elif keep_ordering == 'y':
                break
            else:
                print("Invalid response. Please type 'Y' for Yes or 'N' for No.")

    # Print out the customer's order
    print("This is what we are preparing for you.\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    total_price = 0
    for order in orders:
        item_name = order["Item name"]
        price = order["Price"]
        quantity = order["Quantity"]
        total_price += price * quantity
        print(f"{item_name:24} | ${price:<6.2f} | {quantity}")

    # Print total price
    print(f"\nTotal: ${total_price:.2f}")

if __name__ == "__main__":
    main()
