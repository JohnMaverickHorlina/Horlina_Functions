 #Food Ordering System

def display_menu():
    print("\nBenvenuto to Maverick's Trattoria")
    print("\nOur menu:")
    print("1. Lasagna: ₱150")
    print("2. Pizza Margherita: ₱350")
    print("3. Pizza capricciosa: ₱350")
    print("4. Pizza quattro formaggi: ₱350")
    print("5. Spaghetti Carbonara: ₱200")
    print("6. Tiramisu: ₱100")
    print("7. Chianti wine: ₱100")

def get_user_input(prompt, cast_type):
    
    while True:
        user_input = input(prompt).strip()
        if cast_type == int:
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid number.")
        elif cast_type == float:
            if user_input.replace('.', '', 1).isdigit():  
                return float(user_input)
            else:
                print("Invalid input. Please enter a valid number.")

def main():
    # Menu prices
    prices = {
        1: 150,
        2: 350,
        3: 350,
        4: 350,
        5: 200,
        6: 100,
        7: 100,
    }

    # Display the menu
    display_menu()

    # Initialize total cost
    total_cost = 0

    # Take user input for the order
    while True:
        choice = get_user_input("\nEnter the number of the item you'd like to order (or 0 to finish): ", int)
        if choice == 0:
            break
        elif choice in prices:
            total_cost += prices[choice]
            print(f"Added item {choice} to your order. Current total: ₱{total_cost:.2f}")
        else:
            print("Invalid choice. Please select a valid menu item.")

    # Ensure at least one item was ordered
    if total_cost == 0:
        print("\nYou did not order anything. Goodbye!")
        return

    # Process payment
    while True:
        cash = get_user_input(f"\nYour total is ₱{total_cost:.2f}. Enter the amount of cash rendered: ", float)
        if cash >= total_cost:
            change = cash - total_cost
            print(f"\nGRACIAS!For ordering,Your change is ₱{change:.2f}. Buona giornata!")
            break
        else:
            print("Insufficient cash. Please enter an amount equal to or greater than the total cost.")

if __name__ == "__main__":
    main()