from transformers import pipeline

def translate_text(text):
    try:
        translator = pipeline("translation_en_to_fr")
        translation = translator(text)[0]["translation_text"]
        return translation
    except Exception:
        return None