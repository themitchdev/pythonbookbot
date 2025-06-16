from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    try:    
        path = f"{sys.argv[1]}"
        words = num_words(get_book_text(path))
    

        my_dict = char_and_count(get_book_text(path))
    

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        sorted_my_dict = sort_dict(my_dict)
        for item in sorted_my_dict:
            if item[0].isalpha():
                print(f"{item[0]}: {item[1]}")
        print("============= END ===============")

    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
if __name__=="__main__":
    main()   
