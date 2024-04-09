def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower = get_number_of_letter(text)
    print(lower)




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_letter(text):
    lower = text.lower()
    char = [*lower]
    count = {}
    for c in char:
        count[char[c]] = 1
        if char[c] in count:
            count[char[c]] += 1
                
    return char

main()