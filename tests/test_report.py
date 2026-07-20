import io
import unittest
from contextlib import redirect_stdout

from bookbot.report import build_report, print_report


class ReportTest(unittest.TestCase):
    def test_build_report_includes_summary_stats(self) -> None:
        report = build_report(
            "book.txt",
            501,
            {"b": 2, "1": 50, "a": 4, "!": 10},
        )

        self.assertIn("Words: 501", report)
        self.assertIn("Letters analyzed: 6", report)
        self.assertIn("Unique letters: 2", report)
        self.assertIn("Most common letter: a (4)", report)
        self.assertIn("Approx. reading time: 3 minutes", report)

    def test_build_report_handles_text_without_letters(self) -> None:
        report = build_report("book.txt", 2, {"1": 3, "!": 1})

        self.assertIn("Letters analyzed: 0", report)
        self.assertIn("Unique letters: 0", report)
        self.assertIn("Most common letter: N/A", report)

    def test_print_report_formats_large_numbers_and_filters_non_letters(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            print_report(
                "book.txt",
                1234,
                {"a": 1000, "b": 234, "1": 50, "!": 10},
            )

        report = output.getvalue()
        table_section = report.split("Char   Count    Percent", 1)[1]
        table_section = table_section.split("============= END REPORT", 1)[0]

        self.assertIn("Words: 1,234", report)
        self.assertIn("Letters analyzed: 1,234", report)
        self.assertIn("Unique letters: 2", report)
        self.assertIn("Most common letter: a (1,000)", report)
        self.assertIn("Approx. reading time: 5 minutes", report)
        self.assertIn("a      1,000     81.04%", report)
        self.assertIn("b        234     18.96%", report)
        self.assertNotRegex(table_section, r"(?m)^1\s")
        self.assertNotRegex(table_section, r"(?m)^!\s")


if __name__ == "__main__":
    unittest.main()
