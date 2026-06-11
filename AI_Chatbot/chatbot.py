import json
import random
import re
import os

# Loading responses from JSON file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "responses.json"), "r") as f:
    RESPONSES = json.load(f)


def preprocess(text: str) -> str:
    """Lowercase and remove punctuation from user input."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def get_response(user_message: str) -> str:
    """
    Match the user message against known patterns using simple keyword search.
    Returns a random matching response or a default fallback.
    """
    cleaned = preprocess(user_message)

    # Scoring each category by how many pattern words appear in the message
    best_category = None
    best_score = 0

    for category, data in RESPONSES.items():
        if category == "default":
            continue
        patterns = data.get("patterns", [])
        score = sum(1 for pattern in patterns if pattern in cleaned)
        if score > best_score:
            best_score = score
            best_category = category

    if best_category and best_score > 0:
        return random.choice(RESPONSES[best_category]["responses"])

    # Fallback
    return random.choice(RESPONSES["default"]["responses"])


if __name__ == "__main__":
    # Quick local test
    test_inputs = ["Hello", "What is machine learning?", "Bye", "Tell me about Python"]
    for msg in test_inputs:
        print(f"User: {msg}")
        print(f"Bot : {get_response(msg)}\n")
