from stats import get_num_words

from stats import counting_chars
from stats import get_book_text

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    word_count = get_num_words(path)
    print(f"{word_count} words found in the document")

    char_counts = counting_chars(text)

    # Print the character counts
    print(char_counts)


main()
