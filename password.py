def check_password(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short (min 8 characters).")

    has_upper = has_lower = has_digit = has_special = False
    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_upper:
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if has_lower:
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if has_digit:
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if has_special:
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")

    if strength == 5:
        rating = "Very Strong"
    elif strength >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

user_password = input("Enter a password to test: ")
rating, suggestions = check_password(user_password)

print("\nPassword Strength:", rating)
if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print("-", s)
