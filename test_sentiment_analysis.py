import unittest
from sentiment_analysis import analyze_sentiment


class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        text = "I love this product! It's amazing."
        result = analyze_sentiment(text)
        self.assertIsNotNone(result)
        self.assertIn(result["label"], ["POSITIVE", "NEGATIVE"])
        self.assertGreaterEqual(result["score"], 0.5)

    def test_invalid_input(self):
        self.assertIsNone(analyze_sentiment(""))
        self.assertIsNone(analyze_sentiment(123))


if __name__ == '__main__':
    unittest.main()