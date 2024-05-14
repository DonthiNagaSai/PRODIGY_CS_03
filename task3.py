import re

def assess_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numbers = any(char.isdigit() for char in password)
    special_chars = bool(re.match('[!@#$%^&*(),.?":{}|<>]', password))

    strength = 0

    if length >= 8:
        strength += 1
    if uppercase:
        strength += 1
    if lowercase:
        strength += 1
    if numbers:
        strength += 1
    if special_chars:
        strength += 1

    return strength

def main():
    password = input("Enter your password to assess its strength: ")
    strength = assess_password_strength(password)

    if strength == 5:
        print("Password is very strong.")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    else:
        print("Password is weak.")

if __name__ == "__main__":
    main()