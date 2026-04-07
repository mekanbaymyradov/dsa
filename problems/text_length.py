"""
The input file contains text. A word is considered to be a sequence of non-white characters running in a row. Words are separated by one or more spaces, line translations, or end-of-line characters.

Determine how much various the words are contained in this text.
"""

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    pass
    text = sys.stdin.read()
    words = text.split()
    unique_words = set(words)
    print(len(unique_words))


if __name__ == '__main__':
    main()