from stats import get_word_count, get_char_count, sortdict, sort_format
import sys


def get_book_text(path):
    
    

    with open(path) as f:
        contents = f.read()



    return contents





def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()

    count = get_word_count(text)
    
    sortedDict = sortdict(get_char_count(text))

    string = sort_format(get_char_count(text))

    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {path}...\n" \
    "----------- Word Count ----------\n" \
    f"Found {count} total words\n" \
    "--------- Character Count -------\n" \
    f"{string}")

    




main()