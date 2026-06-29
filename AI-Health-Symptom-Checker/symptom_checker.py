import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# All possible symptoms (must match dataset columns)
ALL_SYMPTOMS = [
    "fever", "cough", "headache", "fatigue", "nausea",
    "sore_throat", "runny_nose", "body_ache", "vomiting",
    "diarrhea", "chest_pain", "shortness_of_breath"
]

def load_and_train():
    """Load dataset and train the ML model."""
    df = pd.read_csv("dataset.csv")

    X = df[ALL_SYMPTOMS]
    y = df["disease"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100

    return model, df, accuracy

def get_user_symptoms():
    """Prompt user to enter symptoms and return as a clean list."""
    print("\n" + "="*50)
    print("Available symptoms to choose from:")
    for i, s in enumerate(ALL_SYMPTOMS, 1):
        print(f"  {i}. {s.replace('_', ' ').title()}")
    print("="*50)

    raw = input("\nEnter your symptoms (comma-separated, e.g. fever, cough): ")
    entered = [s.strip().lower().replace(" ", "_") for s in raw.split(",")]

    # Validate symptoms
    valid = [s for s in entered if s in ALL_SYMPTOMS]
    invalid = [s for s in entered if s not in ALL_SYMPTOMS]

    if invalid:
        print(f"\n⚠️  These symptoms were not recognized and will be ignored: {', '.join(invalid)}")

    if not valid:
        print("❌ No valid symptoms entered. Please try again.")
        return get_user_symptoms()

    return valid

def predict_disease(model, user_symptoms):
    """Convert user symptoms to feature vector and predict disease."""
    # Build input vector
    input_vector = [1 if s in user_symptoms else 0 for s in ALL_SYMPTOMS]
    input_df = pd.DataFrame([input_vector], columns=ALL_SYMPTOMS)

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    confidence = round(max(probabilities) * 100, 2)

    return prediction, confidence, input_vector
