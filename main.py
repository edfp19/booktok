from stats import num_words, character_count, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

relative_path= sys.argv[1]
sorted_dict = sort_dict(relative_path)
print(f"============ BOOKBOT ============\n Analyzing book found at {relative_path}...")
print("----------- Word Count ----------")
num_words(relative_path)
print("--------- Character Count -------")
for dictionary in sorted_dict:
    print(f"{dictionary["key"]}: {dictionary["num"]}")