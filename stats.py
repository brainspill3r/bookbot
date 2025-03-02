def get_num_words(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def counting_chars(text):
    chars_dict = {}

    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
