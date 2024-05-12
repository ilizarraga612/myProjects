'''
Author: Isabelle Lizarraga
Class: CSC 120
Description: This program will take in a one line description
of a "city street". Then it prints a version of it based on
the charcters,height,width provided of the building.
'''
class Building:
    '''
    AN object of this class reps a building
    _width: represents building width
    _height represents building height
    _brick: represents the character that will make the building
    __init_: initializes width,height,brick values
    get_height: getter method for height value
    get_width: getter method for width
    at_height: returns building at a specified height
    '''
    def __init__(self, width, height, brick):
        self._width = int(width)
        self._height = int(height)
        self._brick = brick

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def at_height(self, height):
        # checks if the height is not > than building
        if height in range(self._height):
            # prints building
            return self._brick * self._width
        else:
            return ' ' * self._width

class Park:
    '''
    An object of class Park represents a park
    _width: represents total width of park
    _foliage: represents the character of the leaves
    __init__: initializes width and foliage atributes
    get_width: getter for widht val
    at_height: returns line for park at certain height
    '''
    def __init__(self, width, foliage):
        self._width = int(width)
        self._foliage = foliage

    def get_width(self):
        return self._width

    def at_height(self, height):
        if height in [0, 1, 4]:
            # find middle of park
            middle = self._width // 2
            if height == 4:
                # add single char to middle of park
                return ' ' * (middle + 1) + str(self._foliage) + ' ' * (middle)
            else:
                # does the same as line 61 but with different characters
                return ' ' * (middle + 1) + '|' + ' ' * middle
        elif height == 2:
            # compute the middle of the park
            middle = self._width // 2 - 1
            # insert the 5 characters in middle of park at height 2
            return ' ' * middle + str(self._foliage) * 5 + ' ' * (middle - 1)
        elif height == 3:
            middle = self._width // 2
            # insert the 3 characters in middle of park at height 3
            return ' ' * middle + str(self._foliage) * 3 + ' ' * (middle - 1)
        else:
            # return empty spaces
            return ' ' * (self._width + 1)


class EmptyLot:
    '''
    An object of class EmptyLot is an empty lot
    _width: represents width of empty lot
    _trash: are chars used to rep thr trash in empty lot
    __init__:initializes width and trash vals
    get_width: getter for empty lot width
    at_height: returns line for empty lot at certain height
    '''
    def __init__(self, width, trash):
        self._width = int(width)
        self._trash = trash

    def get_width(self):
        return self._width

    def at_height(self, height):
        # replace any "_" with " "
        if '_' in self._trash:
            self._trash = self._trash.replace('_', ' ')
        if height == 0:
            # only return chars that fit in width of emptylot
            return (self._trash * self._width)[:self._width]
        elif height > 0:
            # return empty spaces if the height>0
            return ' ' * (self._width - 1)

def info(st):
    '''
    Recurses through street specs,add infrastructures, as an object to new list
    st: list of building,parks,empty lots in specified street
    returns: new list with all objects created for the specified street
    '''
    # base case
    if st == []:
        return []
    # adds new object to a list
    elif len(st) == 1:
        return [determine_obj(st[0])]
    else:
        # adds new object to a list recursively
        return [determine_obj(st[0])] + info(st[1:])

def determine_obj(line):
    '''
    Creates object for each one specified in street descript
    Parameters: string from list of given street spec
    Returns: object that corresponds with specs
    '''
    street = line.split(',')
    # check if it is a building
    if street[0][0] == 'b':
        # return building object
        return Building(street[0][2:], street[1], street[2])
    # check if a park
    elif street[0][0] == 'p':
        # return park object
        return Park(street[0][2:], street[1])
    # check if empty lot
    elif street[0][0] == 'e':
        # return an empty lot object
        return EmptyLot(street[0][2:], street[1])

def building_height(st):
    '''
    Recurses through list of given specs, creates new list with the heights.
    :param st: list of buildings,parks,empty lots in a given street
    :return: list w/heights of all buildings,parks,empty lots
    '''
    # base case
    if st == []:
        return []
    elif len(st) == 1:
        # find height for building
        if st[0][0] == 'b':
            street = st[0].split(',')
            return [street[1]]
        # all parks have height 5
        elif st[0][0] == 'p':
            return [5]
        # all empty lots are of height 1
        else:
            return [1]
    else:
        # adds height of infrastructure to the new list
        if st[0][0] == 'b':
            street = st[0].split(',')
            return [int(street[1])] + building_height(st[1:])
        elif st[0][0] == 'p':
            return [5] + building_height(st[1:])
        else:
            return [1] + building_height(st[1:])


def max_height(heights):
    '''
    Recurses through list of heights to find max height
    :param heights: list w/heights of buildings,parks,empty lots in street
    :return: max height in heights[]
    '''
    # base case
    if heights == []:
        return 1
    elif len(heights) == 1:
        return heights[0]
    else:
        # set max value
        value = max_height(heights[1:])
        # compare max value with a value from the list
        if int(heights[0]) >= int(value):
            # return value from the list if > max val
            return heights[0]
        else:
            # if max value > return value
            return value

def total_width(st):
    '''
    Recurses through list of given specs for stree and add width for
    each infrastructure object
    :param st: is list of all buildings, parks,empty lots in given street
    :return: sum of the width of all elems in given specs
    '''
    # base case
    if st == []:
        return 0
    elif len(st) == 1:
        street = st[0].split(',')
        return int(street[0][2:])
    else:
        # split the string by comma
        street = st[0].split(',')
        # add the width of the elements recursively
        return int(street[0][2:]) + total_width(st[1:])

def print_street_at_height(specs, height):
    '''
    Joins all elems so they are able to be printed at once
    :param specs: list of infrastructure objects
    :param height: max height of buildings,parks,empty lots
    :return: street in correct form w/all elems at a certain height
    '''
    # base case
    if specs == []:
        return ''
    else:
        # print elems of one object
        print(specs[0].at_height(height), end='')
        # recurses
        return print_street_at_height(specs[1:], height)

def height_at(specs, max):
    '''
    Recurses through height to print out each line
    :param specs: list of all infrastructures
    :param max: max height of buildings and such objects
    :return: prints the street lines
    '''
    # base case
    if max == -1:
        return
    else:
        print('|', end='')
        # print line by line
        print_street_at_height(specs, max)
        print('|')
        # recurse in descending order
        height_at(specs, max - 1)

def main():
    design = input('Street: ')
    street = design.split()
    # list of all street objects
    specs = info(street)
    # list of all heights
    heights = building_height(street)
    # max height
    max_h = int(max_height(heights))
    # total width of street
    total_w = total_width(street)
    print('+' + '-' * (total_w) + '+')
    # print each line recursively
    height_at(specs, max_h)
    print('+' + '-' * (total_w) + '+')
main()