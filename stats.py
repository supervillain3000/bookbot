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
