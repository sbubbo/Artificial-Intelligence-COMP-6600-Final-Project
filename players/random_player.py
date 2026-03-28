import random
from game.board import *

def random_player(board):
    valid_cols = [col for col in range(COLS) if is_valid_location(board, col)]
    return random.choice(valid_cols)