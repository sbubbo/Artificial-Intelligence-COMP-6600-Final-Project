"""
Create a greedy player ai that will pick the first available column to drop its token in.
Once it has a token in the board, it will try to put more tokens in the same column or adjacent columns to try to win.
If the greedy player can win in the next move, it will pick that column.
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