import random
import string

def generate_password(length=8, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special=True):
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    number_chars = string.digits
    special_chars = string.punctuation

    # Build the pool of characters
    char_pool = ''
    if include_uppercase:
        char_pool += uppercase_chars
    if include_lowercase:
        char_pool += lowercase_chars
    if include_numbers:
        char_pool += number_chars
    if include_special:
        char_pool += special_chars

    # Ensure there's at least one character type selected
    if not char_pool:
        raise ValueError("At least one character type must be selected")

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
