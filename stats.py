import sys

def get_book_text(path):
    
    with open(path) as f:
        return f.read()

def get_word_count(text):
    
	return len(text.split())

def get_char_counts(text):

    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:

        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(items):
   
    return items["num"]

def generate_report(filepath):
    """Reads a book and prints a formatted report of its statistics."""
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    book_text = get_book_text(filepath)
    
    # --- Print Word Count ---
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # --- Print Character Count ---
    char_counts = get_char_counts(book_text)
    
    # Convert the dictionary into a list of dictionaries for sorting
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list in descending order using the sort_on helper function
    char_list.sort(reverse=True, key=sort_on)
    
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 your_script_name.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    generate_report(path_to_file)





