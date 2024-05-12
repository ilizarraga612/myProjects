'''
Author: Isabelle Lizarraga
Class: CSC 120
Description: This program will reconstruct a tree from a given
inorder traversal. Then it will find & return the postorder
traversal w/ its decoded val sequence.
'''
class BinaryTree:
    '''
    An object of this class represents a node that contains a
    value, and a reference to its 'left child' and its 'right
    child'.
    Attributes:
    _value: value at node
    _lchild: reference to left node
    _rchild: reference to right node
    Methods:
    add_right_value: sets val for right node
    add_left_value: sets val for left node
    '''

    def __init__(self, value):
        '''
        initializes tree values
        :param value: the root of tree
        '''
        self._value = value
        self._lchild = None
        self._rchild = None

    def get_value(self):
        return self._value

    def get_l(self):
        return self._lchild

    def get_r(self):
        return self._rchild

    def add_right_val(self, val):
        '''
        adds right value to right tree
        :param val: val to be added to right tree
        :return: none
        '''
        self._rchild = val

    def add_left_value(self, val):
        '''
        adds the left value to the left tree
        :param val: val to be added to left
        :return: none
        '''
        self._lchild = val


def decoded_tree(preorder, inorder):
    '''
    Recursively go through given preorder and inorder traversals
    to build tree
    Parameters:
    preorder: list of the given preorder description of the tree,
    inorder: list that contains the given inorder of tree
    Returns: binary tree decoded from the given preorder/inorder
    '''
    if len(preorder) < 1 or len(inorder) < 1:
        return None
    else:
        # finds root
        root = preorder[0]
        # find root in inorder list
        idx = inorder.index(root)
        new_tree = BinaryTree(root)
        # add the values to the left and right nodes for each node
        new_tree.add_left_value(decoded_tree(preorder[1:idx + 1],
                                             inorder[:idx]))
        new_tree.add_right_val(decoded_tree(preorder[idx + 1:],
                                            inorder[idx + 1:]))
    return new_tree


def post(tree):
    '''
    Traverse through tree w/postorder
    Parameter:
    tree: binary tree created from the pre/inorder
    traversals
    Returns:
    A string that is the postorder tree.
    '''
    if tree == None:
        return ''
    else:
        # left child node + right child node + parent to get
        # postorder
        return post(tree.get_l()) + post(tree.get_r()) + ' ' + tree.get_value()

def decode_sequence(encoded, tree):
    '''
    Decode the encoded sequence of vals
    Parameters:
    encoded: string of encoded sequence of values
    tree: tree created from the pre/inorder traversals.
    '''
    sequence = ''
    i = 0
    # set cur to root
    cur = tree
    encoded = encoded.strip()
    while i < len(encoded):
        # see if goes left or right
        if int(encoded[i]) == 0:
            if cur._lchild == None:
                cur = tree
            else:
                cur = cur._lchild
        elif int(encoded[i]) == 1:
            if cur._rchild == None:
                cur = tree
            else:
                cur = cur._rchild
        # checks if leaf node
        if cur._rchild == None and cur._lchild == None:
            sequence += cur._value
            cur = tree
        i += 1
    print(sequence)


def main():
    file = input('Input file: ')
    infile = open(file, 'r').readlines()

    preorder = infile[0].split()
    inorder = infile[1].split()
    encoded = infile[2]
    # create tree
    tree = decoded_tree(preorder, inorder)
    # find postorder
    postorder = post(tree)
    print(postorder)
    print('')
    decode_sequence(encoded, tree)
main()
