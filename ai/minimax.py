"""
This file sets up the Connect Four minimax algorithm for the AI player

Functions of this file include: 
 - score_board: gives the board a number score so minimax knows how good a position is
 - minimax: the recursive minimax algorithm that looks ahead and picks the best move for the AI player
"""

#import everything from board.py
import sys
sys.path.append('..')
from game.board import *

#scoring function for minimax to evaluate board
#the higher the score the better the position for the AI player, lower if better for humna, 0 if roughly equal
def score_board(board):
    if winning_move(board, AI): #return a very high score for good AI position, calls function from board.py
        return 100000
    elif winning_move(board, PLAYER): #return low score if human wins
        return -100000
    else:
        return 0 #neutral score for non-winning positions
    

""" MINIMAX ALGORITHM """
def minimax(board, depth, maximizing): #maximixing returns true if AI turn, false if human

    #base case: stop recursing if game over or depth limit reached
    #column is None because we are not returning a move, just a score for the position since base case
    if winning_move(board, AI):
        return (None, 100000) #return very high score for good AI position
    if winning_move(board, PLAYER):
        return (None, -100000) #return low score if human wins
    if is_board_full(board):
        return (None, 0) #neutral score for draw
    if depth == 0:
        return None, score_board(board) #evaluate non-terminal position with scoring function
    
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
                new_score = minimax(temp_board, depth-1, False)[1] #recurse with depth-1 and minimizing for human's turn

                if new_score > best_score: #if this move is better than is best score so far
                    best_score = new_score
                    best_col = col

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
                new_score = minimax(temp_board, depth-1, True)[1] #recurse with depth-1 and maximizing for AI's turn

                if new_score < best_score: #if this move is worse than is best score for human
                    best_score = new_score
                    best_col = col

        return best_col, best_score
