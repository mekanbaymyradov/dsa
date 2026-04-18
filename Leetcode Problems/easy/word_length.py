import sys


def main():
    text = sys.stdin.read()
    words = text.split()
    unique_words = set(words)
    print(len(unique_words))


if __name__ == '__main__':
    main()