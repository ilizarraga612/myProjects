### Author: Isabelle Lizarraga
### Class: CSC 110 002
### Description: This program will take the contents of a file and convert them into an infographic.
### It consists of 7 functions that each return values that are later indexed in the main function in order
### to calculate the dimensions and individual displays of the infographic.
from graphics import graphics
def read_file(file_name):
    '''

    :param file_name: pulls whatever text file was entered into the input under the main
    :return: words will be a list of the contents from the text file(file_name)
    This function will open and read the input file and addd each item into a list to be used later
    '''
    file = open(file_name, 'r').readlines()
    words = []
    for line in file:
        line = line.strip('\n').split()
        for word in line:
            words.append(word)
    return words

def count_words(words):
    '''

    :param words: words is a list containing the contents of the input file
    :return: returns a dictionary with each unique word from the text file along with the value(# of times it appears)
    This function will loop through words to initially add the word as a key and from there tally how many times it
    occurs in the word list
    '''
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        elif word in dict:
            dict[word] += 1
    return dict

def word_list(dict):
    '''

    :param dict: is the dictionary of key(unique words) and values(count of how many times the word is used)
    :return: word_list is a list of the unique words that exist in the file, basically 'dict' minus the keys
    Loops through dict to create a list without keys or repeat words
    '''
    word_list = []
    for key in dict:
        if key not in word_list:
            word_list.append(key)
    return word_list

def frequencies(dict):
    '''

    :param dict: is the dictionary of key(unique words) and values(count of how many times the word is used)
    :return: the values small, medium, large represents how many unique words there are of each word length
    This function sorts the words by length and then counts how mnay of each there are in the dictionary
    '''
    small = 0
    medium = 0
    large = 0
    for key, value in dict.items():
        if len(key) >= 0 and len(key) <= 4:
            small += dict[key]
        if len(key) >= 5 and len(key) <= 7:
            medium += dict[key]
        if len(key) >= 8:
            large += dict[key]
    return small,medium, large

def capitalized(dict):
    '''

    :param dict: is the dictionary of key(unique words) and values(count of how many times the word is used)
    :return: Cap and non-cap are the counts of how many of the words are capitalized and non-capitalized
    This function re-establishes the word_list and then checks each word with .isupper for capitalization
    from there is adds the word to either the cap or non-cap count
    '''
    word_list = []
    cap = 0
    noncap = 0
    for key in dict:
        if key not in word_list:
            word_list.append(key)
    for word in word_list:
        if word[0].isupper():
            cap += 1
        else:
            noncap += 1
    return cap,noncap

def punctuation(dict):
    '''

    :param dict: is the dictionary of key(unique words) and values(count of how many times the word is used)
    :return: Punct and nonpunct are the counts of how many words from the word_list contain punctuation
    Based on whether .isalmun() returns True the function will either add a count to nonpunct or punct

    '''
    word_list = []
    punct = 0
    nonpunct = 0
    for key in dict:
        if key not in word_list:
            word_list.append(key)
    for word in word_list:
        if word.isalnum():
            nonpunct += 1
        else:
            punct += 1
    return punct, nonpunct

def most_used(dict):
    '''

    :param dict: is the dictionary of key(unique words) and values(count of how many times the word is used)
    :return: the variable starting with most will return the key or word which was repeated the most, the variables
    ending in winner will return the exact number of times the most word was repeated.
    The function first will sort the keys form the original dictionary into smaller dictionaries based on the key's
    length. Once the small,medium,large dictionaries are established it will add the values of the keys into the
    corresponding lists, ex. the values from the small_dict will be added to the small_values list.
    Then the max function will be used to pluck out the largest values form the individual size lists.
    Lastly the small, medium, large dictionaries will be searched through values for the max value from the lists. If
    the value matches the key it will declare the key the most used and then assign the key's value as the winning tally
    '''
    small_dict ={}
    medium_dict = {}
    large_dict = {}
    small_values = []
    medium_values = []
    large_values = []
    for key, value in dict.items():
        if len(key) >= 0 and len(key) <= 4:
            small_dict[key] = value
        if len(key) >= 5 and len(key) <= 7:
            medium_dict[key] = value
        if len(key) >= 8:
            large_dict[key] = value
    for key, value in small_dict.items():
        small_values.append(value)
        small_winner = max(small_values)
        if small_winner == small_dict[key]:
            most_small = key
    for key,value in medium_dict.items():
        medium_values.append(value)
        medium_winner = max(medium_values)
        if medium_winner == medium_dict[key]:
            most_medium = key
    for key, value in large_dict.items():
        large_values.append(value)
        large_winner = max(large_values)
        if large_winner == large_dict[key]:
            most_large = key
    return most_small, small_winner, most_medium, medium_winner, most_large, large_winner

def main():
    file_name = input('Name for infographic:\n')
    gui = graphics(600, 700, 'Infographic')
    words = read_file(file_name)
    dict = count_words(words)
    most = most_used(dict)
    ''' most_values simplifies what I needed for line 179 it indexes the return values from the most_used function'''
    most_values = 'Most used words (s/m/l):',most[0],'(',most[1],'x)',most[2],\
                   '(',most[3],'x)',most[4],'(',most[5],'x)'
    sml = frequencies(dict)
    cap_noncap = capitalized(dict)
    punct_nonpunct = punctuation(dict)
    unique_words = word_list(dict)
    ''' the following 7 lines are what determine the height of each measure in the bar graphs'''
    smallbar = ((450 / sum(sml)) * sml[0])
    mediumbar = ((450 / sum(sml)) * sml[1])
    largebar = ((450 / sum(sml)) * sml[2])
    capbar = ((450 / sum(cap_noncap)) * cap_noncap[0])
    noncapbar = ((450 / sum(cap_noncap)) * cap_noncap[1])
    punctbar = ((450 / sum(punct_nonpunct)) * punct_nonpunct[0])
    nonpunctbar = ((450 / sum(punct_nonpunct)) * punct_nonpunct[1])
    gui.rectangle(0, 0, 600, 700, 'cadet blue')
    gui.text(40, 20, file_name, 'thistle1', 20)
    gui.text(40, 50, 'Total Unique Words:','thistle1',25)
    gui.text(40,80,most_values,'thistle1',15)
    gui.text(280,50, len(unique_words),'thistle1',25)
    gui.text(40,100,'Word Lengths','white',20)
    gui.rectangle(40,130,95,450,'white')
    gui.rectangle(40,130,95,smallbar,'MediumPurple1')
    gui.text(40,130,'Small words','white',10)
    gui.rectangle(40,(130+smallbar),95,mediumbar,'cornflower blue')
    gui.text(40,(130+smallbar),'Medium words','white',10)
    gui.rectangle(40,(130+smallbar+mediumbar),95,largebar,'MediumPurple1')
    gui.text(40,(130+smallbar+mediumbar),'Large words','white',10)
    gui.text(230,100,'Caps/Non-Cap','white',20)
    gui.rectangle(230,130,95,450,'white')
    gui.rectangle(230,130,95,capbar,'cornflower blue')
    gui.text(230,130,'Capitalized','white',10)
    gui.rectangle(230,(130+capbar),95,noncapbar,'MediumPurple1')
    gui.text(230,(130+capbar),'Non-capitalized','white',10)
    gui.text(420,100,'Punct/Non-Punct','white',20)
    gui.rectangle(420,130,95,450,'white')
    gui.rectangle(420,130,95,punctbar,'MediumPurple1')
    gui.text(420,130,'Punctuated','white',10)
    gui.rectangle(420,(130 + punctbar),95,nonpunctbar,'cornflower blue')
    gui.text(420,(130+punctbar),'Non-punctuated','white',10)
    gui.draw()
main()
