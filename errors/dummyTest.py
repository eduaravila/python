import unittest


def cap_text(text):
    return text.capitalize()


class TestCap(unittest.TestCase):
    def test_cap_text(self):
        text = "eduardo"
        result = cap_text(text)
        self.assertEqual(result, "Eduardo")


unittest.main()
