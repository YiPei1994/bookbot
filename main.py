def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    listed = []
    
    for chars in chars_dict:
        if chars.isalpha():
            new_dict = {}
            new_dict['name'] = chars
            new_dict['num'] = chars_dict[chars]
            listed.append(new_dict)

    sorted_list = sorted(listed, key=lambda k: k.get('num'),reverse=True)

    print('---  Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    print('')
    for dict in sorted_list:
     
        print(f'The "{dict["name"]}" character was found {dict["num"]} times')     

    print('--- End report ---')
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict['num']

main()