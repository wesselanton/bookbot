import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Sequence

from main import main


class MainTest(unittest.TestCase):
    def run_main(self, args: Sequence[str]) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = main(args)

        return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_main_returns_error_for_missing_file(self) -> None:
        exit_code, stdout, stderr = self.run_main(["missing.txt"])

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout, "")
        self.assertIn("Error: could not read 'missing.txt'", stderr)

    def test_main_prints_pretty_report_for_utf8_book(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            book_path = Path(temp_dir) / "book.txt"
            book_path.write_text("Hello hello \u00e6 123!", encoding="utf-8")
            exit_code, stdout, stderr = self.run_main([str(book_path)])

        report = stdout
        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertIn("============ BOOKBOT REPORT ============", report)
        self.assertIn(f"File: {book_path}", report)
        self.assertIn("Summary", report)
        self.assertIn("Words: 4", report)
        self.assertIn("Letters analyzed: 11", report)
        self.assertIn("Unique letters: 5", report)
        self.assertIn("Most common letter: l (4)", report)
        self.assertIn("Approx. reading time: 1 minute", report)
        self.assertIn("Character Frequency", report)
        self.assertIn("Char   Count    Percent", report)
        self.assertIn("l          4     36.36%", report)
        self.assertIn("h          2     18.18%", report)
        self.assertIn("\u00e6          1      9.09%", report)
        self.assertIn("============= END REPORT ==============", report)
        table_section = report.split("Char   Count    Percent", 1)[1]
        table_section = table_section.split("============= END REPORT", 1)[0]
        self.assertNotRegex(table_section, r"(?m)^1\s")
        self.assertNotRegex(table_section, r"(?m)^!\s")

    def test_main_limits_frequency_table_with_top_option(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            book_path = Path(temp_dir) / "book.txt"
            book_path.write_text("aaa bb c d", encoding="utf-8")
            exit_code, stdout, stderr = self.run_main(
                [str(book_path), "--top", "2"])

        table_section = stdout.split("Char   Count    Percent", 1)[1]
        table_section = table_section.split("============= END REPORT", 1)[0]

        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertIn("Character Frequency (top 2)", stdout)
        self.assertRegex(table_section, r"(?m)^a\s+3\s+42\.86%")
        self.assertRegex(table_section, r"(?m)^b\s+2\s+28\.57%")
        self.assertNotRegex(table_section, r"(?m)^c\s")
        self.assertNotRegex(table_section, r"(?m)^d\s")


if __name__ == "__main__":
    unittest.main()
