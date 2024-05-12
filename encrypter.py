### Author: Isabelle Lizarraga
### Class: CSC 110 002
### Description: This program is the first half of a pair.
### It will take the lines in a file and sramble them so that they are encrypted.
### It gets the random placemtnes for the existing lines from the randint function.
### The only input it requires is the name of which file it needs to encrypt
###
def encrypter():
    import random
    random.seed(125)
    file_name = input('Enter a name of a text file to encrypt:\n')
    file = open(file_name,'r')
    read_file = file.readlines()
    index_list = []
    line_count = len(read_file) * 5
    i = 1
    file_list = []
    index_list = []
    lines = len(read_file) - 1

    while i <= len(read_file):
        index_list.append(i)
        i += 1

    for index in range(line_count):
        random_one = random.randint(0, lines)
        random_two = random.randint(0, lines)
        index_list[random_one], index_list[random_two] = index_list[random_two], index_list[random_one]
        read_file[random_one], read_file[random_two] = read_file[random_two], read_file[random_one]
    encrypted_file = open('encrypted.txt', 'w')

    for item in read_file:
        encrypted_file.write(item)
    encrypted_file.close()
    index_file = open('index.txt', 'w')

    for index in index_list:
        index_file.write(str(index) + '\n')
    index_file.close()
encrypter()












