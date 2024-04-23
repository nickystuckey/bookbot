def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = num_words(text)
    char_counts = count_letters(text)
    report = book_report(char_counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for i in report:
        print(f"The {i["letter"]} character was found {i["num"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered = text.lower()
    letter_counts = {}
    for i in lowered:
        if i in letter_counts:
            letter_counts[i] += 1
        else:
            letter_counts[i] = 1
    return letter_counts

def sort_on(dict):
    return dict["num"]

def book_report(counts):
    counts_list = []
    for letter in counts:
        if letter.isalpha():
            temp = {}
            temp["letter"]= letter
            temp["num"]= counts[letter]
            counts_list.append(temp)
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list
                   
main()