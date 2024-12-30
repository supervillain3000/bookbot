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

def sort_on(dict):
    return dict["char"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")
    
    char_counts = count_chars(file_contents)
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The {char} character was found {count} times")
    
    print("--- End report ---")

if __name__ == '__main__':
    main()
