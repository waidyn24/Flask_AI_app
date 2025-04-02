import openai
from typing import Optional, Dict


def analyze_sentiment_with_gpt(text: str, api_key: str) -> Optional[Dict]:
    if not text or not isinstance(text, str):
        return None

    try:
        openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Analyze sentiment of the following text. Respond with JSON format: {\"label\": \"POSITIVE/NEGATIVE/NEUTRAL\", \"score\": 0.0-1.0}"},
                {"role": "user", "content": text}
            ],
            temperature=0.1
        )

        # Парсим JSON из ответа
        import json
        result = json.loads(response.choices[0].message.content)
        return result

    except Exception as e:
        print(f"Error in GPT sentiment analysis: {e}")
        return None