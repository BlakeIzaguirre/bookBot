import sys
from stats import count_words, count_letters, sort_letter_counts

def get_book_text(book_path):
    with open(book_path, "r") as file:
        return file.read()

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
book_text = get_book_text(book_path)
character_counts = count_letters(book_text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {count_words(book_text)} total words")
print("--------- Character Count -------")

sorted_counts = sort_letter_counts(character_counts)
for letter, count in sorted_counts:
    print(f"{letter}: {count}")

print("============= END ===============")