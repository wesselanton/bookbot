# BookBot

BookBot is a small Python command-line application that analyzes UTF-8 text files and prints a readable book report.

It reports word count, letter frequency, the most common letter, and an approximate reading time.

Requires Python 3.9 or newer.

## Usage

```sh
python3 main.py books/frankenstein.txt
```

Show only the most common letters:

```sh
python3 main.py books/frankenstein.txt --top 10
```

Show help:

```sh
python3 main.py --help
```

## Options

- `--top N`: Show only the top `N` letters in the frequency table.

## Running Tests

```sh
python3 -m unittest discover -s tests -v
```

## Project Structure

- `main.py`: Application entry point.
- `bookbot/`: Application package.
- `bookbot/cli.py`: Command-line argument parsing.
- `bookbot/reader.py`: UTF-8 text file reading.
- `bookbot/stats.py`: Word and character statistics.
- `bookbot/report.py`: Report formatting and printing.
- `tests/`: Unit tests.
- `books/`: Sample text files.

## Sample Output

```text
============ BOOKBOT REPORT ============
File: books/frankenstein.txt

Summary
-------
Words: 75,767
Letters analyzed: 337,020
Unique letters: 31
Most common letter: e (44,538)
Approx. reading time: 304 minutes

Character Frequency (top 3)
---------------------------
Char   Count    Percent
e     44,538     13.22%
t     29,493      8.75%
a     25,894      7.68%

============= END REPORT ==============
```
