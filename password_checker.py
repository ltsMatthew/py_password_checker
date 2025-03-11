import re
import getpass

def check_password_strength(password):
    strength = {"length": False, "uppercase": False, "lowercase": False, "digit": False, "special": False}

    if len(password) >= 8:
        strength["length"] = True
    if re.search(r"[A-Z]", password):
        strength["uppercase"] = True
    if re.search(r"[a-z]", password):
        strength["lowercase"] = True
    if re.search(r"\d", password):
        strength["digit"] = True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength["special"] = True

    score = sum(strength.values())

    print("\n **Password Strength Analysis:**")
    for rule, passed in strength.items():
        print(f"- {rule.capitalize()}: {'Pass' if passed else 'Fail'}")

    if score == 5:
        print("\n **Strong Password!**")
    elif 3 <= score < 5:
        print("\n **Moderate Password – Consider Making it Stronger!**")
    else:
        print("\n **Weak Password! Change it Immediately!**")

# Secure password input
password = getpass.getpass("Enter your password: ")
check_password_strength(password)
