import os 

def read_words(file_name: str) -> None: 
    words_count = 0 
    letter_freq = {}
    word_list = []
    with open(file_name) as file: 
        for line in file.readlines():
            word_list.append(line.replace('\n', ''))
    file.close()
    
    # Get number of words
    words_count = len(word_list)

    # Make letter frequency map  
    for word in word_list:
        for letter in word: 
            letter_freq[letter] = letter_freq.get(letter, 0)  + 1

    # Print output 
    line1 = "Number of words: {}".format(words_count) 
    line2 = "Number of occurrences: {}".format(letter_freq)
    print("{}\n{}".format(line1, line2))

def main():
    read_words('words.txt')


if __name__ == '__main__':
    main()