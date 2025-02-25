"""
BookBoot that counts the words in books
"""
import sys
from stats import count_chars, get_num_words

def main():
    """
    Main function
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    try:
        with open(file, "r", encoding='utf-8') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    char_counts = count_chars(file_contents)
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == '__main__':
    main()
