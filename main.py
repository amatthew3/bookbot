from stats import num_words
from stats import characters_found
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
        return file_contents

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    number = num_words(content)
    print (f"Found {number} total words")
    result = characters_found(content)
    sort_dict(result)

main ()


#nicholas
#657-233-9018
#nick-rei@protonmail.com
#name & number
#door code 
