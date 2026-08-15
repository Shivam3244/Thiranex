import re
import hashlib
import os

PASSWORD_DB = "password_history.txt"


def check_length(password):
    return len(password) >= 8


def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))


def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))


def check_digit(password):
    return bool(re.search(r"\d", password))


def check_special(password):
    return bool(re.search(r"[^A-Za-z0-9]", password))


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    return salt.hex(), password_hash.hex()


def is_password_reused(password):
    if not os.path.exists(PASSWORD_DB):
        return False

    with open(PASSWORD_DB, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                salt_hex, stored_hash = line.split(":", 1)
                salt = bytes.fromhex(salt_hex)
                _, calculated_hash = hash_password(password, salt)

                if calculated_hash == stored_hash:
                    return True
            except ValueError:
                continue

    return False


def save_password_hash(password):
    salt_hex, password_hash = hash_password(password)

    with open(PASSWORD_DB, "a", encoding="utf-8") as file:
        file.write(f"{salt_hex}:{password_hash}\n")


def suggest_password():
    return "R7!mQ2#vL9@xP4"


def analyze_password(password):
    checks = {
        "Length (8+ characters)": check_length(password),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Number": check_digit(password),
        "Special character": check_special(password),
    }

    score = sum(checks.values())

    print("\n===== PASSWORD ANALYSIS =====")

    for check, result in checks.items():
        print(f"{check}: {'PASS' if result else 'FAIL'}")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"\nPassword Strength: {strength}")

    if strength in ("Weak", "Moderate"):
        print("Suggested stronger password:")
        print(suggest_password())

    return strength


def main():
    print("================================")
    print("   PASSWORD STRENGTH ANALYZER")
    print("================================")

    password = input("Enter password: ")

    if not password:
        print("Password cannot be empty.")
        return

    analyze_password(password)

    if is_password_reused(password):
        print("\nWarning: This password was used previously.")
    else:
        save = input("\nSave password hash for history? (y/n): ")

        if save.lower() == "y":
            save_password_hash(password)
            print("Password hash saved securely.")

    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
