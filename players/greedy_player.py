"""
Create a greedy player AI.
Takes the most obvious move, which is to try to win immediately by placing a token in a column that would give it 4 in a row.
Once it has a token in the board, it will try to put more tokens in the same column or adjacent columns to try to win.
If the greedy player can win in the next move, it will pick that column.

Looks for the most immediate benefit. If it can build upon existing tokens, it will do that. 
"""
from game.board import *

def greedy_player(board):
    # Try to win immediately
    for col in range(COLS):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_token(board, row, col, AI)

            if winning_move(board, AI):
                board[row][col] = EMPTY  # undo
                return col

            board[row][col] = EMPTY  # undo

    # Otherwise pick first valid column
#    for col in range(COLS):
#        if is_valid_location(board, col):
#            return col
    
    # Otherwise try to build on existing tokens
    for col in range(COLS):
        if is_board_full(board):
            return None  # No valid moves left
        
        #if there are no AI tokens on the board, just pick the first valid column
        if not np.any(board == AI):
            if is_valid_location(board, col):
                return col

        #if there are AI tokens on the board, try to build on them by placing a token in the same column or adjacent columns
        for row in range(ROWS):
            #Need to check if the token belongs to the AI because we only want to build on our own tokens, not the player's tokens
            if board[row][col] == AI:
                #need to check if there are spaces above or beside the AI token to build on it, if there are no spaces then we can't build on that token and we need to check the next one
                if row < ROWS - 1 and board[row + 1][col] == EMPTY:  # check below
                    return col
                if col > 0 and board[row][col - 1] == EMPTY:  # check left
                    return col - 1
                if col < COLS - 1 and board[row][col + 1] == EMPTY:  # check right
                    return col + 1
    # If no winning move or building move is found, pick the first valid column
    for col in range(COLS):
        if is_valid_location(board, col):
            return col


"""

from game.board import *

def greedy_player(board):
    # Try to win immediately
    for col in range(COLS):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_token(board, row, col, AI)

            if winning_move(board, AI):
                board[row][col] = EMPTY  # undo
                return col

            board[row][col] = EMPTY  # undo

    # Otherwise pick first valid column
    for col in range(COLS):
        if is_valid_location(board, col):
            return col

"""