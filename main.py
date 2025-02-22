import sys

def count_chars(text):
    char_dict = {}

    for char in text.strip().lower():
        if char.isspace():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
   
    return (char_dict)
            
def count_words(text):
    text_list = text.split()
    counter = 0

    for word in text_list:
        counter += 1

    return counter

def main():

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
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    char_counts = count_chars(file_contents)
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == '__main__':
    main()
