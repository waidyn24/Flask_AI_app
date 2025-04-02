from flask import Flask, render_template, request, jsonify
from sentiment_analysis import analyze_sentiment
from text_summarizer import summarize_text

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Анализ тональности
    sentiment_result = analyze_sentiment(text)

    # Суммаризация текста
    summary_result = summarize_text(text)

    response = {
        "sentiment": sentiment_result,
        "summary": summary_result
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)