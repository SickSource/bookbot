from stats import get_word_count, char_count, sort_char_counts_to_list
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #file_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    o = get_book_text(file_path)
    n = get_word_count(o)
    counts = char_count(o)
    report = sort_char_counts_to_list(counts)
    
    # Filter to only alphabetical characters
    filtered = [d for d in report if d["char"].isalpha()]
    
    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {n} total words")
    print("--------- Character Count -------")
    for item in filtered:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
