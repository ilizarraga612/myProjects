'''
Author: Isabelle Lizarraga
Class: CSC 120
Description: This program will create/represent one half of
a battleship game. It allows a player 1 to place their ship
pieces on a grid and player 2 will be the guessing player of the game.

'''
import sys

class GridPos:
    '''
    A GridPos object represents a grid position.
    self._x: x coordinate of the position
    self._y: y coordinate of the position
    self._ship: ship object at the coordinate position
    self._guess: boolean val, T if pos has been guessed
    '''
    def __init__(self, x, y):
        '''
        initializes the grid
        :param x: x coord
        :param y: y coord
        '''
        self._x = x
        self._y = y
        self._ship = None
        self._guess = False

    def __str__(self):
        if self._ship == None:
            return 'ー'
        else:
            return str(self._ship)

class Board:
    '''
    Board describes the playing board or grid but with the ships placed.
    self._grid: 10x10 grid where each pos is a GridPos obj
    self._ships: collection of Ship objs
    '''
    def __init__(self, grid, ships):
        '''
        initializes grid and ships
        '''
        self._grid = grid
        self._ships = ships

    def __str__(self):
        i = 0
        while i < len(self._grid):
            print(self._grid[i:i+10])
            i += 10

class Ship:
    '''
    A Ship instance represents a ship for the
    battkleship board.
    self._kind: the ship type
    self._size: ship size
    self._pos: grid positions that said ship is in
    self._safe: # of grid positions of ship
    that are unhit
    '''
    def __init__(self, ship_kind, size, pos, safe):
        self._kind = ship_kind
        self._size = size
        self._pos = pos
        self._safe = safe

    def __str__(self):
        for i in range(self._size):
            print(self._kind)




def errors(ships, placements):
    '''
    Use placemnt file to see if each placement is legal.
    :param ships: 2d list of each line describing a ship
    :param placements: list of line from O.G file
    '''
    ship_list = []
    for ship in ships:
        if ship[0] not in ship_list:
            ship_list.append(ship[0])
        else:
            # if it is print error message then exit
            print("ERROR: fleet composition incorrect")
            sys.exit(0)
    if len(ships) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)

    ship_coords = []
    for ship in ships:
        idx = ships.index(ship)
        # iterate through the positions of each ship
        for elem in ship[1:]:
            # if positions out of range
            if int(elem) > 9 or int(elem) < 0:
                print("ERROR: ship out-of-bounds: " + placements[idx])
                sys.exit(0)
        # check if the ship is placed diagonally
        if ship[1] != ship[3] and ship[2] != ship[4]:
            print("ERROR: ship not horizontal or vertical: " + placements[idx])
            sys.exit(0)
        # see whether ships are overlapping
        else:
            # see if the y coordinates or x coordinates are
            # changing
            if ship[1] == ship[3]:
                point_1, point_2 = int(ship[2]), int(ship[4])
            elif ship[2] == ship[4]:
                point_1, point_2 = int(ship[1]), int(ship[3])
            # check how many spaces it is
            diff = abs(point_1-point_2)
            minimum = min(point_1, point_2)
            for i in range(diff+1):
                coord = [ship[1], minimum+i]
                if coord in ship_coords:
                    print("ERROR: overlapping ship: " + placements[idx])
                    sys.exit(0)
                ship_coords.append(coord)



def main():
    placement = input()
    placements = open(placement, 'r').readlines()
    ships = []
    for line in placements:
        info = line.split()
        ships.append(info)
    check = errors(ships, placements)
    guesses = input()
    list_of_pos = []
    i = 0
    while i<10:
        idx = 0
        while idx<10:
            pos = GridPos(i,idx)
            list_of_pos.append(pos)
            idx += 1
        i += 1
    board = Board(list_of_pos, ships)

main()
