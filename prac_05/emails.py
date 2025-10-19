user_data = {}

while True:
    email = input("Input user email: ").strip()
    if email == "":
        break

    if email in user_data:
        print("This email exist. Please enter a unique email.")
        continue

    name_input = input("Enter your full name: ").strip()
    # Format name using title case
    name_parts = name_input.split()
    formatted_name = " ".join(part.title() for part in name_parts)

    # Confirm name
    confirm = input(f"Is the name '{formatted_name}' correct? (Y/N): ").strip().lower()
    if confirm != 'y':
        print("Let's try again.")
        continue

    # Store using key_to_value format
    key = email
    value = formatted_name
    user_data[key] = value
    print(f"Stored: {key}to{value}")

print("\nFinal user data:")
for email, name in user_data.items():
    print(f"{email}to{name}")