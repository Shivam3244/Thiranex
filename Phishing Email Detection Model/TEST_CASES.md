# Test Cases

## 1. Train the Model

Run:

```bash
python phishing_email_detector.py
```

Expected:
- Dataset loads successfully.
- Model trains without an error.
- Accuracy is displayed.
- Classification report is displayed.
- Confusion matrix is displayed and saved as `confusion_matrix.png`.

## 2. Phishing Email

After training, enter:

```text
URGENT! Your account is suspended. Click http://example.com and verify your password immediately.
```

Expected:
- The model should generally predict `Phishing`.

Note: Machine-learning predictions are not guaranteed; this is an educational model.

## 3. Safe Email

Enter:

```text
The team meeting is scheduled for tomorrow at 10 AM. Please review the agenda before the meeting.
```

Expected:
- The model should generally predict `Safe`.

## 4. Dataset Validation

The program should reject datasets that do not contain:

```text
text
label
```

Valid labels are:

```text
phishing
safe
```

## 5. Confusion Matrix

After training, verify that:

```text
confusion_matrix.png
```

exists in the project directory.
