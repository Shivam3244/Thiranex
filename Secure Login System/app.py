from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
import sqlite3
import re
from pathlib import Path

app = Flask(__name__)
app.config["SECRET_KEY"] = "CHANGE_THIS_IN_PRODUCTION"
bcrypt = Bcrypt(app)

DB_PATH = Path("users.db")


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()


def valid_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", username))


def valid_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


def valid_password(password):
    return (
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"\d", password)
        and re.search(r"[^A-Za-z0-9]", password)
    )


@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not valid_username(username):
            flash("Username must be 3-30 characters and use only letters, numbers, or _.")
            return redirect(url_for("register"))

        if not valid_email(email):
            flash("Enter a valid email address.")
            return redirect(url_for("register"))

        if not valid_password(password):
            flash("Password needs 8+ characters, uppercase, lowercase, number, and special character.")
            return redirect(url_for("register"))

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        connection = get_db()
        try:
            # Parameterized SQL prevents SQL injection.
            connection.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                (username, email, password_hash),
            )
            connection.commit()
        except sqlite3.IntegrityError:
            flash("Username or email is already registered.")
            connection.close()
            return redirect(url_for("register"))

        connection.close()
        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        connection = get_db()
        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        connection.close()

        if user and bcrypt.check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["username"])


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
