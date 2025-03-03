# this is to open the .txt and read its contents 
def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#this is to count the numbers of words
def num_words(relative_path):
    file_contents = get_book_text(relative_path)
    text = file_contents.split()
    num_words = len(text)
    print(f"Found {num_words} total words")

# this is to count the number of characters
def character_count(relative_path):
    file_contents = get_book_text(relative_path)
    array_of_characters = file_contents.lower()
    dictionary = {}
    for char in array_of_characters:
            if char in dictionary and char.isalpha(): 
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary

def sort_on(dict):
    return dict["num"]

def sort_dict(relative_path):
    # first we want to read the data 
    text = character_count(relative_path)
    list_of_dicts = []
    for key, value in text.items():
        list_of_dicts.append({"key":key, "num":value})
        list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    print(list_of_dicts)

