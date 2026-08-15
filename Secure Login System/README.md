# Secure Login System

A Flask-based educational secure login web application demonstrating user registration, bcrypt password hashing, validation, parameterized SQL queries, session-based authentication, and logout.

## Features

- User registration
- Bcrypt password hashing
- Password complexity validation
- Email and username validation
- SQLite database
- Parameterized SQL queries to reduce SQL injection risk
- Session-based authentication
- Protected dashboard
- Logout
- Flash messages for errors and status
- Responsive basic interface

## Technologies

- Python 3
- Flask
- Flask-Bcrypt
- SQLite
- HTML/CSS

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Security Concepts

### Password hashing

Passwords are never stored as plaintext. Flask-Bcrypt creates a bcrypt password hash.

### SQL injection protection

Database values are passed as parameters:

```python
connection.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)
```

User input is not concatenated into SQL statements.

### Session management

After successful authentication, a server-side Flask session identifies the logged-in user. Logout clears the session.

## Production Security Checklist

This project is an educational demonstration. Before production deployment:

- Set a strong random `SECRET_KEY` using an environment variable.
- Use HTTPS.
- Configure secure, HttpOnly and SameSite cookies.
- Add CSRF protection.
- Add login rate limiting / account lockout controls.
- Add secure password reset.
- Consider MFA/2FA.
- Use a production database and proper backups.
- Do not run Flask's development server in production.
- Keep dependencies updated.
- Add security logging and monitoring.

## Project Structure

```text
Secure-Login-System/
├── app.py
├── requirements.txt
├── README.md
├── TEST_CASES.md
├── .gitignore
├── LICENSE
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
└── static/
    └── style.css
```
