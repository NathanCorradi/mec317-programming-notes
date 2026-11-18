def get_formatted_user(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("Enter 'q' at any time to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formmatted_name = get_formatted_user(f_name, l_name)
    print(f"\nHello, {formmatted_name.title()}!")
    escape = input("Would you like to exit? (yes/no): ")
    if escape == 'yes':
        break
    elif escape == 'q':
        break




