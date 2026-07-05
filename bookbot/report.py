from typing import Optional


WORDS_PER_MINUTE = 250


def format_reading_time(word_count: int) -> str:
    """
    Formats the approximate reading time for the given word count.

    Args:
        word_count (int): The number of words in the book.
    """
    minutes = 0
    if word_count > 0:
        minutes = (word_count + WORDS_PER_MINUTE - 1) // WORDS_PER_MINUTE

    if minutes == 1:
        return "1 minute"
    return f"{minutes:,} minutes"


def build_report(
    book_path: str,
    word_count: int,
    char_counts_sorted: list[tuple[str, int]],
    top: Optional[int] = None,
) -> str:
    """
    Builds a report of the word count and character counts for a given book.

    Args:
        book_path (str): The path to the book file.
        word_count (int): The total number of words in the book.
        char_counts_sorted (list[tuple[str, int]]): A sorted list of tuples containing characters and their counts.
        top (Optional[int]): The maximum number of letters to show in the frequency table.
    """
    letter_counts = [
        (char, count)
        for char, count in char_counts_sorted
        if char.isalpha()
    ]
    total_letters = sum(count for _, count in letter_counts)
    unique_letters = len(letter_counts)
    most_common = "N/A"
    if letter_counts:
        most_common_char, most_common_count = letter_counts[0]
        most_common = f"{most_common_char} ({most_common_count:,})"

    displayed_counts = letter_counts
    frequency_title = "Character Frequency"
    if top is not None:
        displayed_counts = letter_counts[:top]
        frequency_title = f"Character Frequency (top {top})"

    report_lines = [
        "============ BOOKBOT REPORT ============",
        f"File: {book_path}",
        "",
        "Summary",
        "-------",
        f"Words: {word_count:,}",
        f"Letters analyzed: {total_letters:,}",
        f"Unique letters: {unique_letters:,}",
        f"Most common letter: {most_common}",
        f"Approx. reading time: {format_reading_time(word_count)}",
        "",
        frequency_title,
        "-" * len(frequency_title),
        "Char   Count    Percent",
    ]

    for char, count in displayed_counts:
        percentage = (count / total_letters * 100) if total_letters else 0
        report_lines.append(f"{char:<4} {count:>7,} {percentage:>9.2f}%")

    report_lines.extend(["", "============= END REPORT =============="])
    return "\n".join(report_lines)


def print_report(
    book_path: str,
    word_count: int,
    char_counts_sorted: list[tuple[str, int]],
    top: Optional[int] = None,
) -> None:
    """
    Prints a report of the word count and character counts for a given book.

    Args:
        book_path (str): The path to the book file.
        word_count (int): The total number of words in the book.
        char_counts_sorted (list[tuple[str, int]]): A sorted list of tuples containing characters and their counts.
        top (Optional[int]): The maximum number of letters to show in the frequency table.
    """
    print(build_report(book_path, word_count, char_counts_sorted, top=top))
