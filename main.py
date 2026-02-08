import re

# Load common passwords
def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Check password strength
def check_password_strength(password):

    score = 0
    suggestions = []

    # Load common passwords
    common_passwords = load_common_passwords()

    # Check common password
    if password.lower() in common_passwords:
        return 0, ["Password is too common. Choose a unique password."]

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions


# Strength level
def get_strength_level(score):

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


# Main program
def main():

    password = input("Enter password to test: ")

    score, suggestions = check_password_strength(password)
    strength = get_strength_level(score)

    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 6")

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("-", s)
    else:
        print("Great password!")


if __name__ == "__main__":
    main()
