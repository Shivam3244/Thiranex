"""
Phishing Email Detection Model
Educational ML project using Scikit-learn.

The included dataset is a small demonstration dataset. For production use,
replace it with a large, representative, reviewed dataset.
"""

import re
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


DATASET = Path("emails_dataset.csv")
MODEL = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=1,
    )),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
])


def add_url_features(text):
    """Return simple URL/keyword features for analysis and demonstration."""
    urls = re.findall(r"https?://\S+|www\.\S+", text.lower())
    urgent_words = re.findall(
        r"\b(urgent|immediately|verify|suspended|password|payment|"
        r"click|claim|winner|reward|confirm)\b",
        text.lower(),
    )
    return {
        "url_count": len(urls),
        "urgent_keyword_count": len(urgent_words),
        "text_length": len(text),
    }


def load_data():
    if not DATASET.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET}. Run the program from its project folder."
        )

    df = pd.read_csv(DATASET)

    required = {"text", "label"}
    if not required.issubset(df.columns):
        raise ValueError("Dataset must contain 'text' and 'label' columns.")

    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].astype(str)
    df["label"] = df["label"].str.lower().str.strip()

    valid_labels = {"phishing", "safe"}
    if not set(df["label"]).issubset(valid_labels):
        raise ValueError("Labels must be 'phishing' or 'safe'.")

    return df


def print_feature_examples(df):
    print("\n--- URL / Keyword Feature Examples ---")
    for text in df["text"].head(5):
        features = add_url_features(text)
        print(features)


def main():
    df = load_data()

    print("==========================================")
    print("       PHISHING EMAIL DETECTION MODEL")
    print("==========================================")
    print(f"Dataset records: {len(df)}")
    print(df["label"].value_counts())

    print_feature_examples(df)

    # Stratified split keeps both classes represented in train/test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"],
        test_size=0.25,
        random_state=42,
        stratify=df["label"],
    )

    MODEL.fit(X_train, y_train)

    predictions = MODEL.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n--- Model Evaluation ---")
    print(f"Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, zero_division=0))

    cm = confusion_matrix(
        y_test,
        predictions,
        labels=["phishing", "safe"],
    )

    print("Confusion Matrix:")
    print(cm)

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Phishing", "Safe"],
    ).plot()
    plt.title("Phishing Email Detection - Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=150)
    plt.show()

    # Interactive example.
    email = input("\nEnter an email to classify (or press Enter to exit): ").strip()

    if email:
        prediction = MODEL.predict([email])[0]
        probabilities = MODEL.predict_proba([email])[0]
        confidence = max(probabilities)

        print(f"\nPrediction: {prediction.title()}")
        print(f"Confidence: {confidence:.2%}")
        print("Extracted features:", add_url_features(email))


if __name__ == "__main__":
    main()
