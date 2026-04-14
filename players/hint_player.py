"""
Create a hint player AI.
This player will provide hints to the user about which column to play in.
The  hint player will do so by using minimax to evaluate the board and determine the best move for the user to make.
The hint player will not actually make a move, it will just provide a hint to the user about which column to play in.
"""

"""
from random import random
from game.board import *

def hint_player(board):
    # This is where the minimax algorithm would go to evaluate the board and determine the best move for the user to make.
    # For now, we will just return a random valid column as a hint.
    valid_cols = [col for col in range(COLS) if is_valid_location(board, col)]
    return random.choice(valid_cols)
"""

from ai.minimax import minimax
from game.board import *

def hint_player(board, depth=4):
    best_score = -100000
    best_col = None

    for col in range(COLS):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            temp_board = board.copy()

            # simulate HUMAN move
            drop_token(temp_board, row, col, PLAYER)

            # now let minimax evaluate from AI's perspective
            # IMPORTANT: next turn is AI → maximizing=True
            score = minimax(temp_board, depth-1, True)[1]

            # since minimax is AI-centric, we invert logic:
            # we want moves that are WORST for AI
            if score < best_score or best_col is None:
                best_score = score
                best_col = col

    return best_col