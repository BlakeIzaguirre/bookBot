def get_book_text(book_name):
    with open(f"books/{book_name}.txt", "r") as file:
        return file.read()


print(get_book_text("frankenstein"))
