# p. 53

def unic_words_count(file_name):

    """Calculate and print the amount of unic words in text file
    ## Parameter: file_name: path to txt file in Unicode
    ## Prints the total number of words, number of unic words,
              count of unic words in descending order in the file_name file
    """

    # File open, read and save in text
    with open(file_name, 'r') as f:
        text = f.read()

    # Remove punctuation
    import re
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»'
    text = re.sub('['+punctuation+']', '', text)

    # Lowercase letters
    text = text.lower()

    # Split text to list of words
    word_list = text.strip().split()

    # Get the unic word's number
    occurs_dict = {}
    for word in word_list:
        # Increment the counter
        occurs_dict[word] = occurs_dict.get(word, 0) + 1

    # Present results
    print(f"File {file_name} has {len(word_list)} words and {len(occurs_dict)} from them are unique")
    print()


    # Get the most frequently used words

    # Transfer dictionary to list of tuples
    occurs_dict_list = list(occurs_dict.items())

    # Get list sorted in reverse order
    occurs_dict_list.sort(key=lambda i: i[1], reverse = True)

    # Show the result
    ignore_list = ['и', 'в', 'на', 'не', 'с', 'что', 'к', 'от', 'за', 'а', 'о', 'то', '–']
    for i in occurs_dict_list:
        # TODO: вывести только первые 100 слов
        if i[0] not in ignore_list:
            print(i[0], ':', i[1])

if __name__ == '__main__':
    unic_words_count('Stalin.txt')


"""
p. 120:
Счетчик вхождений каждого слова увеличивается в процессе перебора. 
Это хороший пример выдающихся возможностей словарей: код прост, 
но поскольку операции со словарями в Python сильно оптимизированы, 
он также достаточно быстро работает. 
Эта схема настолько удобна, что она была стандартизирована в 
классе Counter модуля collections стандартной библиотеки.
https://docs.python.org/3/library/collections.html#collections.Counter
"""
# Find the ten most common words in Hamlet
from collections import Counter
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
# Output
# [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
# ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
