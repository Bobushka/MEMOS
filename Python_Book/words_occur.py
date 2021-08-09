# Example from page 53

def words_occur():
    """Calculate and print the amount of unic words in text file"""

    # Get the file name from keyboard
    # file_name = input("Enter the the file name: ")
    file_name = 'Untitled.txt'

    # File open, read and save in the word_list
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()

    # Get the unic words inclusion's number
    occurs_dict = {}
    for word in word_list[:10]:  # test on first ten
        if word.isalpha:  # why isalpha isn't working?
            print(word)
            # Increment the counter
            occurs_dict[word] = occurs_dict.get(word, 0) + 1

            # Present results
    print("File %s has %d words (%d are unique)" \
          % (file_name, len(word_list), len(occurs_dict)))
    List = [occurs_dict.values].sort(reverse=True)  # how to sort counts?
    print(List)
    print(occurs_dict)


words_occur()