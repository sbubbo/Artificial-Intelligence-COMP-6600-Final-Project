"""
This file sets up the Connect Four minimax algorithm for the AI player

Functions of this file include: 
 - score_board: gives the board a number score so minimax knows how good a position is
 - minimax: the recursive minimax algorithm that looks ahead and picks the best move for the AI player
 - minimax_no_pruning: a version of minimax without alpha-beta pruning for comparison in experiments.py
"""

#import everything from board.py
from game.board import *

from ai.heuristics import *

#scoring function for minimax to evaluate board
#the higher the score the better the position for the AI player, lower if better for humna, 0 if roughly equal
def score_board(board, weights =(1, 1, 10)): #weights for material count, center control, and threat detection
    if winning_move(board, AI): #return a very high score for good AI position, calls function from board.py
        return 100000
    elif winning_move(board, PLAYER): #return low score if human wins
        return -100000
    else:
        material_weight, center_weight, threat_weight = weights
        score = 0
        #material count weighted at 1
        score += material_count(board, AI) * material_weight
        score -= material_count(board, PLAYER) * material_weight

        #center control weighted at 1
        score += center_control(board, AI) * center_weight
        score -= center_control(board, PLAYER) * center_weight

        #threat detection weighted at 10 because blocking and winning and most urgent
        score += threat_detection(board, AI) * threat_weight
        score -= threat_detection(board, PLAYER) * threat_weight

        return score
    

""" MINIMAX ALGORITHM """
def minimax(board, depth, maximizing, alpha = -100000, beta = 100000, weights = (1, 1, 10)): #maximixing returns true if AI turn, false if human, set alpha and beta to very low and high values for alpha-beta pruning

    #base case: stop recursing if game over or depth limit reached
    #column is None because we are not returning a move, just a score for the position since base case
    if winning_move(board, AI):
        return (None, 100000) #return very high score for good AI position
    if winning_move(board, PLAYER):
        return (None, -100000) #return low score if human wins
    if is_board_full(board):
        return (None, 0) #neutral score for draw
    if depth == 0:
        return None, score_board(board, weights) #evaluate non-terminal position with scoring function
    
    #maximizing case: AI's turn
    if maximizing:
        best_score = -100000 #start as low as possible to any score will be better
        best_col = None
    
        for col in range(COLS): #check every column
            if is_valid_location(board, col): #if column is not full
                row = get_next_open_row(board, col) #get next open row
                temp_board = board.copy() #copy the board to simulate the move without affecting original board
                drop_token(temp_board, row, col, AI) #simulate dropping AI token in column

                #this is the recursive call to minimax
                #each call is one level deeper, then switch to minimizing for human turn, and only want score back not column
                new_score = minimax(temp_board, depth-1, False, alpha, beta, weights)[1] #recurse with depth-1 and minimizing for human's turn

                if new_score > best_score: #if this move is better than is best score so far
                    best_score = new_score
                    best_col = col

                #update alpha and check if we can prune
                alpha = max(alpha, best_score) #update alpha to be best score found for maximizing player
                if beta <= alpha: #if beta less than or equal to alpha, we can prune
                    break
            
        #add fallback where no column found
        if best_col is None:
            for col in range(COLS):
                if is_valid_location(board, col):
                    best_col = col
                    break

        return best_col, best_score
    
    #minimizing case: human's turn
    else:
        best_score = 100000 #start as high as possible so any score will be worse
        best_col = None
    
        for col in range(COLS): #check every column
            if is_valid_location(board, col): #if column is not full
                row = get_next_open_row(board, col) #get next open row
                temp_board = board.copy() #copy the board to simulate the move without affecting original board
                drop_token(temp_board, row, col, PLAYER) #simulate dropping human token in column

                #this is the recursive call to minimax
                #each call is one level deeper, then switch to maximizing for AI turn, and only want score back not column
                new_score = minimax(temp_board, depth-1, True, alpha, beta, weights)[1] #recurse with depth-1 and maximizing for AI's turn

                if new_score < best_score: #if this move is worse than is best score for human
                    best_score = new_score
                    best_col = col

                #update beta and check if we can prune
                beta = min(beta, best_score) #update beta for minimizing player
                if beta <= alpha: #can prune if beta less than or equal to alpha
                    break

        #add fallback where no column found
        if best_col is None:
            for col in range(COLS):
                if is_valid_location(board, col):
                    best_col = col
                    break

        return best_col, best_score
    
#minimax without alpha-beta pruning for comparison
def minimax_no_pruning(board, depth, maximizing, weights = (1, 1, 10)):

    #base case identical to minimax
    if winning_move(board, AI):
        return (None, 100000)
    if winning_move(board, PLAYER):
        return (None, -100000)
    if is_board_full(board):
        return (None, 0)
    if depth == 0:
        return None, score_board(board, weights)
    
    #maximizing case: AI's turn
    if maximizing:
        best_score = -100000
        best_col = None
    
        for col in range(COLS):
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                temp_board = board.copy()
                drop_token(temp_board, row, col, AI)

                new_score = minimax_no_pruning(temp_board, depth-1, False, weights)[1]

                if new_score > best_score:
                    best_score = new_score
                    best_col = col
                
                #no alpha pruning here so we check every move (difference from minimax)
            
        if best_col is None:
            for col in range(COLS):
                if is_valid_location(board, col):
                    best_col = col
                    break

        return best_col, best_score
    
    #minimizing case: human's turn
    else:
        best_score = 100000
        best_col = None
    
        for col in range(COLS):
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                temp_board = board.copy()
                drop_token(temp_board, row, col, PLAYER)

                new_score = minimax_no_pruning(temp_board, depth-1, True, weights)[1]

                if new_score < best_score:
                    best_score = new_score
                    best_col = col

                #no beta pruning here so we check every move

        if best_col is None:
            for col in range(COLS):
                if is_valid_location(board, col):
                    best_col = col
                    break

        return best_col, best_score