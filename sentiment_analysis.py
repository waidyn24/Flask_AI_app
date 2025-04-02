from transformers import pipeline
from typing import Optional, Dict


def analyze_sentiment(text: str) -> Optional[Dict]:
    if not text or not isinstance(text, str):
        return None

    try:
        classifier = pipeline("sentiment-analysis")
        result = classifier(text)[0]
        return {
            "label": result["label"],
            "score": result["score"]
        }
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return None