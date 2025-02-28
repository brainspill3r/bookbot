def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"  # This should be the relative path to your file
    text = get_book_text(path)
    print(text)


main()  # Call the main function to execute your program
