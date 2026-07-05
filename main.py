import sys
from typing import Optional, Sequence

from bookbot.cli import parse_args
from bookbot.reader import get_book_text
from bookbot.report import print_report
from bookbot.stats import chars_dict_to_sorted_list, count_characters, count_words


def main(args: Optional[Sequence[str]] = None) -> int:
    """
    Runs the BookBot command-line application.

    Args:
        args (Optional[Sequence[str]]): Command-line arguments to parse.
    """
    cli_args, exit_code = parse_args(args)
    if cli_args is None:
        return exit_code

    try:
        book_text = get_book_text(cli_args.book_path)
    except OSError as error:
        print(
            f"Error: could not read '{cli_args.book_path}': {error.strerror}",
            file=sys.stderr,
        )
        return 1
    except UnicodeDecodeError:
        print(
            f"Error: could not read '{cli_args.book_path}' as UTF-8 text",
            file=sys.stderr,
        )
        return 1

    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_sorted = chars_dict_to_sorted_list(char_counts)
    print_report(
        cli_args.book_path,
        word_count,
        char_counts_sorted,
        top=cli_args.top,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
