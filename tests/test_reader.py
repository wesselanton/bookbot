import tempfile
import unittest
from pathlib import Path

from bookbot.reader import get_book_text


class ReaderTest(unittest.TestCase):
    def test_get_book_text_reads_utf8(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            book_path = Path(temp_dir) / "book.txt"
            book_path.write_text("hello \u00e6\u00f8\u00e5", encoding="utf-8")

            self.assertEqual(get_book_text(str(book_path)), "hello \u00e6\u00f8\u00e5")


if __name__ == "__main__":
    unittest.main()
