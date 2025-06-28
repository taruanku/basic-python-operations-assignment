# personalized_greeting.py

def main():
    # Get first and last name from user
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Create full name
    full_name = f"{first_name} {last_name}"

    # Display greeting
    print(f"\nHello, {full_name}! Welcome to the Python program.")

if __name__ == "__main__":
    main()
