### Author: Isabelle Lizarraga
### Class: CSC 110 002
### Description: This program is the secon dhalf of the encrypter decrypter pair.
### This decryptor part will unscramble whatever the encrypter program scrambled.
### It does this throuhg the required input of what text file needs to be reordered and
### what file the index key was stored in.


def decrypter():
    decrypt_file = input('Enter the name of an encrypted text file:\n')
    index_key = input('Enter the name of the encryption index file:\n')
    decrypt = open(decrypt_file, 'r')
    key = open(index_key, 'r')
    # lines 10-13 opens the previously encrytped file and the key/file with the indexes and then reads the contents
    decrypt_list = []
    decrypt_lines = decrypt.readlines()
    key_lines = key.readlines()
    key_range = len(key_lines)
    i = 0
#
    while i < key_range:
        key_lines[i] = int(key_lines[i].strip('\n'))
        i += 1
    index = 1

    while index <= key_range:
        item = key_lines.index(index)
        decrypt_list.append(decrypt_lines[item])
        index += 1
    decrypted_list = open('decrypted.txt', 'w')

    for line in decrypt_list:
        decrypted_list.write(line)
    decrypted_list.close()
decrypter()
