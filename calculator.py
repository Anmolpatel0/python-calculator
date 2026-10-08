# Interactive Calculator & Unit Converter
# Beginner Python Project

CHOICE_PROMPT = "Enter your choice: "


def get_number(message):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def calculator():
    """Perform basic arithmetic operations."""

    while True:
        print("\n========== CALCULATOR ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Back to Main Menu")

        choice = input(CHOICE_PROMPT)

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("❌ Invalid choice! Please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            print(f"✅ {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"✅ {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"✅ {num1} × {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("❌ Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"✅ {num1} ÷ {num2} = {result}")


def unit_converter():
    """Convert different units."""

    while True:
        print("\n========== UNIT CONVERTER ==========")
        print("1. Kilometers → Miles")
        print("2. Celsius → Fahrenheit")
        print("3. Back to Main Menu")

        choice = input(CHOICE_PROMPT)

        if choice == "3":
            break

        if choice == "1":
            km = get_number("Enter kilometers: ")

            miles = km * 0.621371

            print(f"✅ {km} km = {miles:.2f} miles")

        elif choice == "2":
            celsius = get_number("Enter temperature in Celsius: ")

            fahrenheit = (celsius * 9 / 5) + 32

            print(f"✅ {celsius}°C = {fahrenheit:.2f}°F")

        else:
            print("❌ Invalid choice! Please select 1-3.")


def currency_converter():
    """Convert USD and INR."""

    # Fixed rate for beginner project
    usd_to_inr = 83.50

    while True:
        print("\n========== CURRENCY CONVERTER ==========")
        print("1. USD → INR")
        print("2. INR → USD")
        print("3. Back to Main Menu")

        choice = input(CHOICE_PROMPT)

        if choice == "3":
            break

        if choice == "1":
            usd = get_number("Enter amount in USD: ")

            if usd < 0:
                print("❌ Amount cannot be negative.")
                continue

            inr = usd * usd_to_inr

            print(f"✅ ${usd:.2f} = ₹{inr:.2f}")

        elif choice == "2":
            inr = get_number("Enter amount in INR: ")

            if inr < 0:
                print("❌ Amount cannot be negative.")
                continue

            usd = inr / usd_to_inr

            print(f"✅ ₹{inr:.2f} = ${usd:.2f}")

        else:
            print("❌ Invalid choice! Please select 1-3.")


def main():
    """Main program."""

    while True:
        print("\n")
        print("=" * 40)
        print("   INTERACTIVE CALCULATOR")
        print("   & UNIT CONVERTER")
        print("=" * 40)

        print("\n1. Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("\n" + CHOICE_PROMPT)

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            currency_converter()

        elif choice == "4":
            print("\n👋 Thank you for using the program!")
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-4.")


# Start the program
if __name__ == "__main__":
    main()