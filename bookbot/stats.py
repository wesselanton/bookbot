from collections import Counter
from collections.abc import Mapping


def count_words(book_text: str) -> int:
    """
    Counts the number of words in the given book text.

    Args:
        book_text (str): The text of the book.
    """
    words = book_text.split()
    return len(words)


def count_characters(book_text: str) -> dict[str, int]:
    """
    Counts the number of characters in the given book text.

    Args:
        book_text (str): The text of the book.
    """
    return dict(Counter(book_text.lower()))


def sort_on(char: tuple[str, int]) -> tuple[int, str]:
    """
    Builds a deterministic sort key for a character count.

    Args:
        char (tuple[str, int]): A tuple containing a character and its count.
    """
    character, count = char
    return -count, character


def chars_dict_to_sorted_list(
    characters: Mapping[str, int],
) -> list[tuple[str, int]]:
    """
    Sorts character counts by descending count, then by character.

    Args:
        characters (Mapping[str, int]): Character counts to sort.
    """
    return sorted(characters.items(), key=sort_on)
