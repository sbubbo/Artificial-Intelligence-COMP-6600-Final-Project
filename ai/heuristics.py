"""
This file sets up the Connect Four heuristics

Functions of this file include: 
 - material_count: counts the number of open lines for the player and opponent and gives a score based on the difference
 - center_control: values tokens in center more than those on the sides because they can contribute to wins in more directions
 - threat_detection: detects when a player has 3 in a row with an empty space next to it, which is a critical threat that must be blocked
"""

from game.board import *

def material_count(board, player):
    # this counts how many potential winning lines are open for each of the players

    opponent = 2 if player == 1 else 1

    player_open = 0
    opponent_open = 0

    # Check all possible 4-cell windows
    windows = []

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            windows.append([board[r][c + i] for i in range(4)])

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            windows.append([board[r + i][c] for i in range(4)])

    # Diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            windows.append([board[r + i][c + i] for i in range(4)])

    # Diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS  - 3):
            windows.append([board[r - i][c + i] for i in range(4)])

    # Count open lines
    for window in windows:
        if opponent not in window:
            player_open += 1
        if player not in window:
            opponent_open += 1

    return player_open - opponent_open

def center_control(board, token):
    # considers tokens in the center column more valuable since they can contribute to wins in more directions
    # then considers columsn 2 and 4 the next most valuable, then columns 1 and 5, then columns 0 and 6

    column_scores = [1, 2, 3, 4, 3, 2, 1] #center column worth the most

    score = 0
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == token:
                score += column_scores[col]

    return score

def threat_detection(board, token):
    # detects if a player has 3 in a row with an empty space next to it
    # this is urgent because it means a win is one move away for the opponent, so needs to prioritze blocking

    score = 0

    windows = []

    # horizontal    
    for r in range(ROWS):
        for c in range(COLS - 3):
            windows.append([board[r][c + i] for i in range(4)])

    # vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            windows.append([board[r + i][c] for i in range(4)]) 

    # diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            windows.append([board[r + i][c + i] for i in range(4)]) 


    # diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS  - 3):
            windows.append([board[r - i][c + i] for i in range(4)])
    
    #check each window for 3 in a row with empty space
    for window in windows:
        if window.count(token) == 3 and window.count(EMPTY) == 1: #checks if a group if 4 has exactly three tokens and 1 empty space
            score += 1
    
    return score