Milk_Per_Latte_Gal = 0.25
Bulk_Discount_Rate = 0.10
Pastry_Bundle_Price = 5.00
Tax_Rate = 0.10

Cold_Brew_Price = 6.00
Drip_Price = 3.00


def get_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ['y', 'yes']:
            return True
        elif ans in ['n', 'no']:
            return False
        print("Please enter Y or N.")


def inventory_check():
    print("\n--- Inventory Check ---")

    gallons_in_fridge = get_float("How many gallons of milk are currently in the fridge? ")
    lattes_expected = get_int("How many lattes does the shop expect to sell today? ")

    if gallons_in_fridge < 0 or lattes_expected < 0:
        print("Values cannot be negative. Returning to menu.")
        return

    gallons_needed = lattes_expected * Milk_Per_Latte_Gal
    difference = gallons_in_fridge - gallons_needed

    if difference > 0:
        print("\nStatus: Surplus")
        print(f"Excess milk: {difference:.2f} gallons")
    elif difference == 0:
        print("\nStatus: Exact")
        print("You have exactly the amount of milk needed.")
    else:
        print("\nStatus: Shortage")
        print(f"Additional milk needed: {abs(difference):.2f} gallons")

    print(f"(Milk needed for {lattes_expected} lattes: {gallons_needed:.2f} gallons)\n")


def transaction_calculator():
    print("\n--- Transaction Calculator ---")

    print("Drink Options:")
    print("1) Specialty Cold Brew ($6)")
    print("2) Standard Drip ($3)")

    while True:
        drink_choice = input("Select drink type (1 or 2): ").strip()
        if drink_choice == "1":
            drink_name = "Specialty Cold Brew"
            price_each = Cold_Brew_Price
            break
        elif drink_choice == "2":
            drink_name = "Standard Drip"
            price_each = Drip_Price
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    qty = get_int("Enter the number of drinks being purchased: ")
    if qty < 0:
        print("Quantity cannot be negative. Returning to menu.")
        return

    subtotal = qty * price_each

    discount = 0.0
    if qty >= 10:
        discount = subtotal * Bulk_Discount_Rate
        subtotal -= discount

    wants_pastry = get_yes_no("Add a Pastry Bundle for $5? (Y/N): ")
    if wants_pastry:
        subtotal += Pastry_Bundle_Price

    tax = subtotal * Tax_Rate
    total_due = subtotal + tax   # FIXED

    print("\n--- Receipt ---")
    print(f"Drink: {drink_name}")
    print(f"Quantity: {qty}")
    if discount > 0:
        print(f"Bulk Discount applied: -${discount:.2f}")
    if wants_pastry:
        print(f"Pastry Bundle added: +${Pastry_Bundle_Price:.2f}")
    print(f"Subtotal (before tax): ${subtotal:.2f}")
    print(f"Barista Service Tax (10%): ${tax:.2f}")
    print(f"Total Due: ${total_due:.2f}\n")

    amount_paid = get_float("Enter amount paid by customer: $")

    if amount_paid < total_due:
        print("Error: Amount paid is less than total due. Transaction cannot be completed.\n")
    elif amount_paid == total_due:
        print("Exact amount received. Thank You!\n")
    else:
        change = amount_paid - total_due
        print(f"Payment Accepted. Change due: ${change:.2f}\n")


def main():
    while True:
        print("=== Katelyns C(offee) - PA2 ===")
        print("1) Inventory Check")
        print("2) Transaction Calculator")
        print("3) Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            inventory_check()
        elif choice == "2":
            transaction_calculator()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()