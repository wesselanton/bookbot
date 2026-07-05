import unittest

from bookbot.stats import chars_dict_to_sorted_list, count_characters, count_words


class StatsTest(unittest.TestCase):
    def test_count_words(self) -> None:
        self.assertEqual(count_words("one two\nthree"), 3)

    def test_count_characters_lowercases_text(self) -> None:
        self.assertEqual(count_characters("AaB!"), {"a": 2, "b": 1, "!": 1})

    def test_chars_dict_to_sorted_list_sorts_by_count_descending(self) -> None:
        self.assertEqual(
            chars_dict_to_sorted_list({"a": 2, "b": 5, "c": 1}),
            [("b", 5), ("a", 2), ("c", 1)],
        )


if __name__ == "__main__":
    unittest.main()
