from stats import chars_dict_to_sorted_list, count_characters, count_words
import sys


def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book from a given file path and returns it as a string.

    Args:
        filepath (str): The path to the book file.
    """

    with open(filepath) as file:
        return file.read()


def print_report(book_path: str, word_count: int, char_counts_sorted: list[tuple[str, int]]):
    """
    Prints a report of the word count and character counts for a given book.

    Args:
        book_path (str): The path to the book file.
        word_count (int): The total number of words in the book.
        char_counts_sorted (list[tuple[str, int]]): A sorted list of tuples containing characters and their counts.
    """
    print(f"Report for {book_path}:")
    print(f"Found {word_count} total words")
    print("Character counts (sorted):")
    for char, count in char_counts_sorted:
        if not char.isalnum():  # Skip non-alphanumeric characters
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


def main():
    """
    Main function to execute the program.
    """

    if len(sys.argv) < 2:
        print("Please provide the path to the book file as a command-line argument. Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    char_counts_sorted = chars_dict_to_sorted_list(char_counts)
    print_report(book_path, word_count, char_counts_sorted)


if __name__ == "__main__":
    main()
