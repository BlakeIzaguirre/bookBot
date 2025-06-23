def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():  # Only count letters, not spaces, punctuation, etc.
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

# this sort gave me so much trouble

def sort_letter_counts(letter_counts):
    return [(str(x[0]), x[1]) for x in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)]

