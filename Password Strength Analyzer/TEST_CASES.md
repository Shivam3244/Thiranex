# Test Cases

## 1. Strong Password
Input: `Hello123!`

Expected: `Password Strength: Very Strong`

## 2. Weak Password
Input: `hello`

Expected: `Password Strength: Weak` and a stronger suggestion.

## 3. Password Reuse
Run the program, save a password hash, then run it again with the same password.

Expected: `Warning: This password was used previously.`

## 4. Empty Password
Press Enter without entering a password.

Expected: `Password cannot be empty.`
