# Test Cases

## 1. Registration

1. Open `/register`.
2. Enter a valid username, email and strong password.
3. Submit.

Expected:
- Registration succeeds.
- User is redirected to login.
- `users.db` is created locally.
- Password is stored as a bcrypt hash, not plaintext.

## 2. Invalid Password

Try:

```text
password
```

Expected:
- Registration is rejected because it lacks the required complexity.

## 3. Login

Use the registered username and password.

Expected:
- User is redirected to `/dashboard`.

## 4. Wrong Password

Use a correct username and incorrect password.

Expected:

```text
Invalid username or password.
```

## 5. Protected Dashboard

Open `/dashboard` without logging in.

Expected:
- User is redirected to `/login`.

## 6. Logout

Click Logout.

Expected:
- Session is cleared.
- User is redirected to login.
- Dashboard is no longer accessible without authentication.

## 7. Duplicate Account

Register the same username or email twice.

Expected:
- Second registration is rejected.

## 8. SQL Injection Basic Check

Try a username such as:

```text
' OR '1'='1
```

Expected:
- It is treated as ordinary input.
- It does not bypass authentication.
