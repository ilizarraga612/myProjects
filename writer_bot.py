'''
Author: Isabelle Lizarraga
Class: CSC 120
Description: This program uses the Markov chain algorithm
to generate a random text. This random text will model the
style/pattern of the original given text.
'''
import random

SEED = 8
random.seed(SEED)
NONWORD = ' '

def data(file, n):
    '''
    Opens txt file and creates a list w/all files info
    Parameters:
    file:user-given file to process
    n:size of the prefix.
    Returns:
    text: single list that contains words from file
    '''
    infile = open(file, 'r').readlines()
    text = []
    for i in range(n):
        text.append(NONWORD)
    for line in infile:
        line = line.split()
        for item in line:
            text.append(item)
    return text

def table(text, n):
    '''
    Creates a 'table' that has each prefix and the suffixes
    that go w/specific prefix.
    Parameters:
    text: list of all words from file
    n: prefix size
    Returns:
    word_dict: dict w/each prefix as key, list of all its
    suffixes as value
    '''
    word_dict = {}
    i = 0
    while i < len(text):
        prefix = tuple(text[i:n + i])
        # check if the suffix for that prefix won't go out of range
        if n + i in range(len(text)):
            if prefix not in word_dict:
                word_dict[prefix] = [text[n + i]]
            else:
                # if already in the dict append suffix to
                # existing list of suffixes
                word_dict[prefix].append(text[n + i])
        i += 1
    return word_dict

def markov_text(word_dict, text, n):
    '''
    Constructs phrases by randomly choosing a suffix for
    a given prefix from word_dict.
    Parameters:
    word_dict: dict w/each prefix as key and a list of all its
    suffixes as value
    n: prefix size
    Returns:
    tlist: list of strs of the randomly generated
    text.
    '''
    word_num = input()
    tlist = []
    # first words from the list that are not nonwords
    first_words = text[n:n + n]
    for word in first_words:
        tlist.append(word)
    prefix = tuple(first_words)
    while prefix in word_dict and len(tlist) < int(word_num):
        # check that there is only one suffix
        if len(word_dict[prefix]) == 1:
            suffix = word_dict[prefix][0]
        else:
            idx = random.randint(0, len(word_dict[prefix]) - 1)
            # create a variable for that suffix
            suffix = word_dict[prefix][idx]
        tlist.append(suffix)
        # create the next tuple
        prefix = prefix[1:] + (suffix,)
    return tlist

def output(tlist):
    '''
    Process Markov text, print out list of generated
    text 10 wrds per line
    Parameters:
    tlist: list containing words of the randomly gen txt
    Returns: None
    Prints out a line from the Markov text
    '''
    output_list = []
    # see how many lines(that have 10 wds)
    iter = len(tlist) // 10
    if len(tlist) % 10 != 0:
        iter += 1
    for i in range(iter):
        output_list.append(tlist[:10])
        # remove 1st 10 wrds from list to iter through it
        tlist = tlist[10:]
    # prints
    for list in output_list:
        for word in list:
            print(word, end=' ')
        print('')

def main():
    sfile = input()
    n = int(input())
    text = data(sfile, n)
    word_dict = table(text, n)
    tlist = markov_text(word_dict, text, n)
    output(tlist)


main()