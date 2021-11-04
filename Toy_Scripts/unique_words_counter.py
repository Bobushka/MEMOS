import re


def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text


def prepare_text(text):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»№0123456789'
    text = re.sub('[' + punctuation + ']', '', text)  # Remove punctuation
    text = text.lower()  # Lowercase letters
    return text.strip().split()  # Split text to list of words


def words_count(list_of_words):
    words_dict = {}
    for word in list_of_words:
        # Increment the counter
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


def print_results(f_Name, w_List, o_Dict):
    print(f"File {f_Name} has {len(w_List)} words and {len(o_Dict)} from them are unique", "\n")
    occurs_dict_list = list(o_Dict.items())  # Transfer dictionary to list of tuples
    occurs_dict_list.sort(key=lambda i: i[1], reverse = True)  # Sort list in reverse order
    for i in occurs_dict_list[:100]:  # Show the first 100 most frequently used words
        print(i[0], ':', i[1])


def main(file_name):
    text = read_file(file_name)
    word_list = prepare_text(text)
    occurs_dict = words_count(word_list)
    print_results(file_name, word_list, occurs_dict)
            

if __name__ == '__main__':
    main('text.txt')