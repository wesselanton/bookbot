import argparse
import sys
from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class CliArgs:
    """
    Parsed command-line arguments for BookBot.
    """

    book_path: str
    top: Optional[int]


def positive_int(value: str) -> int:
    """
    Converts a command-line value to a positive integer.

    Args:
        value (str): The command-line value to convert.
    """
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be a positive integer") from error

    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def build_parser() -> argparse.ArgumentParser:
    """
    Builds the command-line argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="python3 main.py",
        description="Analyze a UTF-8 text file and print a readable book report.",
        epilog=(
            "Examples:\n"
            "  python3 main.py books/frankenstein.txt\n"
            "  python3 main.py books/frankenstein.txt --top 10"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "book_path",
        help="Path to the UTF-8 text file to analyze.",
    )
    parser.add_argument(
        "--top",
        metavar="N",
        type=positive_int,
        help="Show only the top N letters in the frequency table.",
    )
    return parser


def get_parser_exit_code(error: SystemExit) -> int:
    """
    Gets a numeric exit code from argparse's SystemExit exception.

    Args:
        error (SystemExit): The exception raised by argparse.
    """
    if isinstance(error.code, int):
        return error.code
    if error.code is None:
        return 0
    return 1


def parse_args(args: Optional[Sequence[str]] = None) -> tuple[Optional[CliArgs], int]:
    """
    Parses command-line arguments without exiting the process.

    Args:
        args (Optional[Sequence[str]]): Command-line arguments to parse.
    """
    parser = build_parser()
    try:
        namespace = parser.parse_args(args)
    except SystemExit as error:
        return None, get_parser_exit_code(error)

    parsed_values = vars(namespace)
    book_path_arg: object = parsed_values.get("book_path")
    top_arg: object = parsed_values.get("top")

    if not isinstance(book_path_arg, str):
        print("Error: book path must be a string", file=sys.stderr)
        return None, 1

    if top_arg is None:
        top = None
    elif isinstance(top_arg, int):
        top = top_arg
    else:
        print("Error: --top must be a positive integer", file=sys.stderr)
        return None, 1

    return CliArgs(book_path=book_path_arg, top=top), 0
