"""
Create a minimax player AI.
This player will use the minimax algorithm to determine the best move to make.
"""

from ai.minimax import minimax
from game.board import *

def minimax_player(board, depth=4):
    best_score = -100000
    best_col = None

    #create a minimax player that uses the minimax algorithm to evaluate the board and determine the best move for the AI to make. 
    # The minimax player will look ahead a certain number of moves (depth) and evaluate the board at each level of the tree to 
    # determine the best move for the AI to make. The minimax player will return the column that it thinks is the best move for the 
    # AI to make.
    for col in range(COLS):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            temp_board = board.copy()

            # simulate AI move
            drop_token(temp_board, row, col, AI)

            # now let minimax evaluate from HUMAN's perspective
            # IMPORTANT: next turn is HUMAN → maximizing=False
            score = minimax(temp_board, depth-1, False)[1]

            if score > best_score or best_col is None:
                best_score = score
                best_col = col
    return best_col