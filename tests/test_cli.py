import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from typing import Optional, Sequence

from bookbot.cli import CliArgs, parse_args


class CliTest(unittest.TestCase):
    def parse_with_output(
        self,
        args: Sequence[str],
    ) -> tuple[Optional[CliArgs], int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            cli_args, exit_code = parse_args(args)

        return cli_args, exit_code, stdout.getvalue(), stderr.getvalue()

    def test_parse_args_returns_book_path(self) -> None:
        cli_args, exit_code, stdout, stderr = self.parse_with_output(
            ["books/frankenstein.txt"]
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "")
        self.assertEqual(stderr, "")
        self.assertIsNotNone(cli_args)
        if cli_args is not None:
            self.assertEqual(cli_args.book_path, "books/frankenstein.txt")
            self.assertIsNone(cli_args.top)

    def test_parse_args_returns_top_option(self) -> None:
        cli_args, exit_code, stdout, stderr = self.parse_with_output(
            ["books/frankenstein.txt", "--top", "10"]
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "")
        self.assertEqual(stderr, "")
        self.assertIsNotNone(cli_args)
        if cli_args is not None:
            self.assertEqual(cli_args.book_path, "books/frankenstein.txt")
            self.assertEqual(cli_args.top, 10)

    def test_parse_args_returns_error_for_missing_argument(self) -> None:
        cli_args, exit_code, stdout, stderr = self.parse_with_output([])

        self.assertIsNone(cli_args)
        self.assertEqual(exit_code, 2)
        self.assertEqual(stdout, "")
        self.assertIn("usage: python3 main.py", stderr)
        self.assertIn(
            "the following arguments are required: book_path", stderr)

    def test_parse_args_prints_help(self) -> None:
        cli_args, exit_code, stdout, stderr = self.parse_with_output([
                                                                     "--help"])

        self.assertIsNone(cli_args)
        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertIn("Analyze a UTF-8 text file", stdout)
        self.assertIn("--top N", stdout)
        self.assertIn("Examples:", stdout)

    def test_parse_args_returns_error_for_invalid_top(self) -> None:
        cli_args, exit_code, stdout, stderr = self.parse_with_output(
            ["book.txt", "--top", "0"]
        )

        self.assertIsNone(cli_args)
        self.assertEqual(exit_code, 2)
        self.assertEqual(stdout, "")
        self.assertIn("must be a positive integer", stderr)


if __name__ == "__main__":
    unittest.main()
