from transformers import pipeline
from typing import Optional


def summarize_text(text: str) -> Optional[str]:
    if not text or not isinstance(text, str) or len(text) < 30:
        return None

    try:
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

        # Ограничиваем входной текст 1024 символами
        truncated_text = text[:1024]

        result = summarizer(
            truncated_text,
            max_length=130,
            min_length=30,
            do_sample=False
        )

        return result[0]["summary_text"]
    except Exception as e:
        print(f"Error in text summarization: {e}")
        return None