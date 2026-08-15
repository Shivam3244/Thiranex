# Phishing Email Detection Model

A machine-learning mini project that classifies email text as **Phishing** or **Safe** using Scikit-learn.

## Features

- Loads a labeled phishing/legitimate email dataset
- Extracts TF-IDF text features
- Detects simple URL and urgency-keyword features for analysis
- Trains a Logistic Regression classifier
- Uses a stratified train/test split
- Displays accuracy
- Displays a classification report
- Generates and saves a confusion matrix
- Allows interactive email prediction

## Technologies

- Python 3
- Pandas
- Scikit-learn
- Matplotlib
- Regular Expressions

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python phishing_email_detector.py
```

The program creates:

```text
confusion_matrix.png
```

after model evaluation.

## Dataset

`emails_dataset.csv` is a small educational demonstration dataset containing labeled examples of phishing and safe emails.

For a real-world model, use a much larger, representative, legally obtained and carefully reviewed dataset. Do not treat the demo dataset's accuracy as evidence of production performance.

## Model

The project uses:

1. TF-IDF vectorization for textual features.
2. Word and bigram features.
3. Logistic Regression for classification.
4. A stratified train/test split.
5. Accuracy, classification report, and confusion matrix for evaluation.

## Example

```text
Dataset records: 40

--- Model Evaluation ---
Accuracy: ...

Classification Report:
              precision    recall  f1-score   support

    phishing       ...
         safe       ...

Confusion Matrix:
[[... ...]
 [... ...]]
```

## Important Limitations

- The included dataset is intentionally small and educational.
- Accuracy can vary with the train/test split.
- High accuracy on a small dataset does not mean the model is production-ready.
- Real phishing detection should combine multiple signals and be tested on unseen, realistic data.
- Never use this project to automatically make high-impact decisions without appropriate human review and security testing.

## Project Structure

```text
Phishing-Email-Detection-Model/
├── phishing_email_detector.py
├── emails_dataset.csv
├── README.md
├── TEST_CASES.md
├── requirements.txt
├── .gitignore
└── LICENSE
```
