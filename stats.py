def get_word_count(book_text):
    words = book_text.split()
    count = 0
    for word in words:
        count += 1
    return count

def char_count(book_text):
    char_counts = {}

    for char in book_text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

#def sort_dictionary_of_characters(char_count_dict):
#    return dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True))

def sort_char_counts_to_list(char_count_dict):
    """Convert a char->count dict to a list of {'char': c, 'num': n} dicts sorted by num desc.

    Uses a helper function and the list .sort() method as required.
    """
    items = []
    for c, n in char_count_dict.items():
        items.append({"char": c, "num": n})

    def _num_key(d):
        return d["num"]

    items.sort(key=_num_key, reverse=True)
    return items