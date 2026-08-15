# Password Strength Analyzer

A Python tool that evaluates the strength of user-entered passwords.

## Features

- Password length and complexity checking
- Uppercase, lowercase, number, and special-character validation
- Password strength classification
- Strong password suggestion
- PBKDF2-HMAC-SHA256 hashing with a random salt
- Optional password-history/reuse checking

## Requirements

Python 3.x. No external packages are required.

## Run

```bash
python password_strength_analyzer.py
```

On some systems:

```bash
python3 password_strength_analyzer.py
```

## Example

```text
================================
   PASSWORD STRENGTH ANALYZER
================================
Enter password: Hello123!

===== PASSWORD ANALYSIS =====
Length (8+ characters): PASS
Uppercase letter: PASS
Lowercase letter: PASS
Number: PASS
Special character: PASS

Password Strength: Very Strong
```

## Security Concepts

- Password complexity validation
- Password hashing
- Random salts
- PBKDF2-HMAC-SHA256
- Password reuse prevention
- Regular expressions

## Important Security Note

This is an educational project. Production authentication should use a dedicated password-hashing library such as Argon2id, scrypt, or bcrypt, along with rate limiting, secure recovery, and MFA.

`password_history.txt` is ignored by Git and should never be committed.
