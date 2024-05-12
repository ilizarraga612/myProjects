###
### Author: Isabelle Lizarraga
### Class: CSC 110 002
### Description: This program is a simplified version of a chess game.
# It requires inputs of position(which will determine the piece they move)
# and direction(which will be either left or right).
# A few of the functions monitor the gameplay such as if the selected move is valid and whether the game is over.
# Three of the functions(move, king_move, knight_move) are in charge of changing the positions of the pieces. Move
# judges if the move_knight or king_move function needs to be called based on player the character it finds 'i' or 'n'.
#


from graphics import graphics

# You should use these globals in the functions in this file!
W_KNIGHT = 'WKn'
W_KING = 'WKi'
B_KNIGHT = 'BKn'
B_KING = 'BKi'
EMPTY = '   '
WHITE = 'White'
BLACK = 'Black'
LEFT = 'l'
RIGHT = 'r'


def is_valid_move(board, position, player):
    if board[position][0] == player[0] and 0 <= position <= 8:
        return True
    else:
        return False



def move_knight(board, position, direction):
    ''' This one works by checking first which color knight is moving. Then based on the direction the user chose it
    will make sure the knight does not move out of bounds. So for the black knight on the right side it cannot
    complete a movement that will make its position greater than nine because then its position would be of the board.
    And so on with the rest of the knights.

     '''
    if board[position] == W_KNIGHT:
        if direction == LEFT:
            if position - 2 >= 0:
                board[position - 2] = W_KNIGHT
                board[position] = EMPTY
        elif direction == RIGHT:
            if position + 2 < 9:
                board[position + 2] = W_KNIGHT
                board[position] = EMPTY
    elif board[position] == B_KNIGHT:
        if direction == LEFT:
            if position - 2 >= 0:
                board[position - 2] = B_KNIGHT
                board[position] = EMPTY
        elif direction == RIGHT:
            if position + 2 < 9:
                board[position + 2] = B_KNIGHT
                board[position] = EMPTY

def move_king(board, position, direction):
    ''' Similar to the move knight function move king checks which color is being played.
     Then depending on which direction was chosen it will ensure the king does not move out of bounds
     and that when it comes across another piece it will replace it
     '''
    if board[position] == W_KING:
        if direction == RIGHT:
            i = position + 1
            if i == 9:
                i = 8
            while board[i] == EMPTY and i < 8:
                i += 1
            board[position] = EMPTY
            board[i] = W_KING

        elif direction == LEFT:
            i = position - 1
            while board[i] == EMPTY and 0 < i:
                i -= 1
            board[position] = EMPTY
            board[i] = W_KING


    elif board[position] == B_KING:
        if direction == LEFT:
           i = position - 1
           if i == 9:
               i = 8
           while board[i] == EMPTY and 0 < i:
               i -= 1
           board[position] = EMPTY
           board[i] = B_KING
        elif direction == RIGHT:
            i = position + 1
            while board[i] == EMPTY and i < 8:
                i += 1
            board[position] = EMPTY
            board[i] = B_KING

def print_board(board):
    ''' Creates the starting board with white pieces on the left and black pieces on the right.
    The board indexes allow the board to change as moves are played later in the game
    '''
    print("+-----------------------------------------------------+")
    print("| " + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ', end='')
    print(board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print('+-----------------------------------------------------+')

def draw_board(board, gui):
    '''
    This controls the graphics portion of the chess board.
    The while loop creates the lines to separate the pieces.
    The for loop goes through board to print out the text with the appropriate colors and piece names.
    gui.clear is at the top so that the board updates each time drawboard is called in the while loop of the main.
    '''
    gui.clear()
    gui.rectangle(65, 110, 520, 50, 'dark red')
    i = 0
    x = 65
    y = 110
    gui.text(225, 50, '1 Dimensional Chess', 'green', 25)
    while i < 8:

        gui.line(x, y, x,y+45, 'black', 1)
        i += 1
        x += 65
    x2 = 65
    y2 = 120
    for i in range(len(board)):
        if board[i] == W_KNIGHT:
            gui.text(x2,y2,'knight','white',15)
        elif board[i] == W_KING:
            gui.text(x2,y2,'king','white',15)
        elif board[i] == B_KNIGHT:
            gui.text(x2,y2,'knight','black',15)
        elif board[i] == B_KING:
            gui.text(x2,y2,'king','black',15)
        x2 += 59

def is_game_over(board):
    ''' '''

    if W_KING not in board:
        print_board(board)
        print('Black wins!')
        return True
    elif B_KING not in board:
        print_board(board)
        print('White wins!')
        return True
    else:
        return False

def move(board, position, direction):
    if board[position][2] == 'i':
        move_king(board, position, direction)
    elif board[position][2] == 'n':
        move_knight(board, position, direction)

    ''' Implement. '''

def main():
    # DO NOT CHANGE THE CODE IN THE MAIN FUNCTION

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)


main()


