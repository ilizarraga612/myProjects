### Author: Isabelle Lizarraga
### Class: CSC 120 001
### Description: This program uses the classes created
### in the linked_list file to organize names with
### their corresponding friends and finds the
### common friends between two inputed names

# imports linked list file
from linked_list import *

def read_file():
    '''
    reads in and opens text file
    reads in the two friend names
    creates 1st linked list of names and their friends
    :return:
    name_list: ll of input names and their friends
    to be used for finding common friends in
    friends_in_common()
    '''
    file_name = input('Input file: ')
    file = open(file_name,'r').readlines()
    name_list = LinkedList()
    for line in file:
        line = line.strip('\n')
        line = line.split()
        friend_1 = Node(line[0])
        friend_2 = Node(line[1])
        # adds friend if name is also in line
        if name_list.in_list(line[0]) != True:
            name_list.add(friend_1)
            name_list.add_main(line[0], line[1])
        else:
            name_list.add_main(line[0], line[1])
        if name_list.in_list(line[1]) != True:
            name_list.add(friend_2)
            name_list.add_main(line[1], line[0])
        else:
            name_list.add_main(line[1], line[0])
    return name_list


def friends_in_common(name_list):
    '''
    Uses the ll name_list to find and organize common friends
    between the two input names.
    Then prints them out in alphabetical order
    :param name_list: the linked list that has the friends of
    the 2 input names
    :return: will print out the common
    friends in alphabetical order

    '''
    list = []
    name_1 = input('Name 1: ').strip()
    name_2 = input('Name 2: ').strip()
    if name_list.in_list(name_1) != True:
        # error message if name1 not known
        print('ERROR: Unknown person ' + name_1)
    elif name_list.in_list(name_2) != True:
        # error message if name2 not known
        print('ERROR: Unknown person ' + name_2)
    else:
        common_friends = LinkedList()
        node1 = name_list.find_main(name_1)
        node2 = name_list.find_main(name_2)
        look_for = node1.first_name()
        while look_for != None:
            find = node2.first_name()
            while find != None:
                if find._main == look_for._main:
                    common_friends.add(Node(look_for))
                find = find._next
            look_for = look_for._next
        if common_friends._head != None:
            print('Friends in common:\n')
            curr = common_friends._head
            while curr != None:
                i = str(curr)
                list.append(i.strip('\n'))
                curr = curr._next
            for item in sorted(list):
                print(item)

def main():
    name_list = read_file()
    friends_in_common(name_list)
main()