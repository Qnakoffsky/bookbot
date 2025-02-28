import os
import sys

from stats import count_words, yanking_my_pizzle, sort_char_counts

def get_book_text(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_file_path = os.path.join(script_dir, file_path)
    with open(abs_file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    getting_numbers_out = get_book_text(book_path)
    character_counts = yanking_my_pizzle(getting_numbers_out)  
    sorted_char_counts = sort_char_counts(character_counts)
    words_count = count_words(getting_numbers_out)
    
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()