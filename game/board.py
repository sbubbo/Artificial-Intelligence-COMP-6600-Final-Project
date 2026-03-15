"""
This file sets up the Connect Four game board and its functions

The functions of this module include:
 - create_board: creates the game board
 - drop_token: drops a token into the board
 - is_valid_location: checks if a location is valid for dropping a token
 - get_next_open_row: gets the next open row in a column
 - print_board: prints the game board
- winning_move: checks if a player has won the game
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

#WINNING MOVE DETECTION
#need to check for four in a row in each direction (horizontal, vertical, diagonal)
def winning_move(board, token):
    #first check horizontal locations for a win
    for row in range(ROWS):
        for col in range(COLS - 3): #we only check to column 3 becayse columns 4, 5, and 6 do not have three more columns to the right of them
            if (board[row][col] == token and
                board[row][col+1] == token and
                board[row][col+2] == token and
                board[row][col+3] == token):
                return True
            
    #next check vertical locations for a win
    for row in range(ROWS - 3): #same logic as above, we only check to row 2 because rows 3, 4, and 5 do not have three more rows below them
        for col in range(COLS):
            if (board[row][col] == token and
                board[row+1][col] == token and
                board[row+2][col] == token and
                board[row+3][col] == token):
                return True
            
    #check diagonal (first check for diagonals that go up and to the right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == token and
                board[row+1][col+1] == token and #incementing both row and col by 1 to check the next diagonal
                board[row+2][col+2] == token and
                board[row+3][col+3] == token):
                return True
    
    #check diagonal (now check for diagonals that go up and to the left)
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if (board[row][col] == token and
                board[row+1][col-1] == token and
                board[row+2][col-2] == token and
                board[row+3][col-3] == token):
                return True

    #if nothing found
    return False

