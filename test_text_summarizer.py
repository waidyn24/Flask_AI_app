import unittest
from text_summarizer import summarize_text


class TestTextSummarizer(unittest.TestCase):
    def test_summarization(self):
        text = """
        Artificial intelligence is transforming many industries, from healthcare to finance. 
        While the benefits are numerous, there are also ethical concerns that need to be addressed. 
        Companies implementing AI solutions must consider privacy, bias, and accountability issues.
        """
        summary = summarize_text(text)
        self.assertIsNotNone(summary)
        self.assertTrue(len(summary) > 0)
        self.assertTrue(len(summary) <= 130)

    def test_invalid_input(self):
        self.assertIsNone(summarize_text(""))
        self.assertIsNone(summarize_text("Short text"))
        self.assertIsNone(summarize_text(123))


if __name__ == '__main__':
    unittest.main()