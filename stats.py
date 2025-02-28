def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def num_words(relative_path):
    file_contents = get_book_text(relative_path)
    text = file_contents.split()
    num_words = len(text)
    print(f"{num_words} words found in the document")

def character_count(relative_path):
    file_contents = get_book_text(relative_path)
    array_of_characters = file_contents.lower()
    dictionary = {}
    for char in array_of_characters:
            if char in dictionary: 
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary