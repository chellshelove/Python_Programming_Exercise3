# Get input mobile phone number from the user
phone_number = input("Enter the mobile phone number (format: 010-0000-0000): ")

# Remove dashes by replacing them with an empty string
cleaned_number = phone_number.replace("-", "")

# Print the cleaned phone number
print(f"Phone number without dashes: {cleaned_number}")