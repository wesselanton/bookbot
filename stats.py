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
    character_count: dict[str, int] = {}
    for char in book_text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(char: tuple[str, int]) -> int:
    """
    Sorts the character count dictionary based on the count of characters.

    Args:
        char (tuple[str, int]): A tuple containing a character and its count.
    """
    return char[1]


def chars_dict_to_sorted_list(characters: dict[str, int]) -> list[tuple[str, int]]:
    """
    Converts the character count dictionary to a sorted list of tuples.

    Args:
        characters (dict[str, int]): A dictionary containing characters and their counts.
    """
    return sorted(characters.items(), key=sort_on, reverse=True)
