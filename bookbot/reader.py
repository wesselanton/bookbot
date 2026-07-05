def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book from a given file path and returns it as a string.

    Args:
        filepath (str): The path to the book file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read()
