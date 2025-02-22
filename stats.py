"Functions used by BookBot"
def count_chars(text):
    "Function that counts chars"
    char_dict = {}

    for char in text.strip().lower():
        if char.isspace():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
 
def get_num_words(text):
    "Function that counts number of words"
    text_list = text.split()
    counter = 0

    for _ in text_list:
        counter += 1

    return counter
