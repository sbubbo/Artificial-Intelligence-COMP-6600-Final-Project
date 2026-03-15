"""
This file sets up the Connect Four game board and its functions

The functions of this module include:
 - create_board: creates the game board
 - drop_token: drops a token into the board
 - is_valid_location: checks if a location is valid for dropping a token
 - get_next_open_row: gets the next open row in a column
 - print_board: prints the game board
"""

import numpy as np

# set up board dimensions
ROWS = 6
COLS = 7

# set player tokens
EMPTY = 0
PLAYER = 1
AI = 2

#creates empty 6x7 game board 
def create_board():
    board = np.zeros((ROWS,COLS), dtype=int)
    return board

# drops a token on the boardat given position
def drop_token(board, row, col, token):
    board[row][col] = token

#checks if top row of clumn is empty which means that the column is not full
def is_valid_location(board, col):
    return board[ROWS-1][col] == EMPTY

# gets lowest empty row in a column because tokens fall to the lowest position (gravity)
def get_next_open_row(board, col):
    for row in range(ROWS):
        if board[row][col] == EMPTY:
            return row
        
#print board with row 0 at the bottom and row 5 at the top
#we flip the the board because when a token is dropped it goes to row 0
# but in Connect Four row 0 is actually the bottom of the board
def print_board(board):
    print(np.flip(board, 0))
    print(" 0 1 2 3 4 5 6")
