"""
This file sets up the Connect Four game and loop

Functions of this file include: 
 - game_loop: alternates between player 1 and player 2 picking a column to drop their token, 
              then checking for a win until someone wins or the board is full
"""

#import everything from board.py
from game.board import *

#import minimax algorithm for AI player
from ai.minimax import minimax

#main game loop
def game_loop():
    board = create_board() #fresh board at the start of game
    print_board(board)
    game_over = False
    turn = 0 #player 1 goes first

    while not game_over: #continues to loop as long as no one has one and board is not full
        if turn % 2 == 0: #player 1's turn
            turn_token = PLAYER
            turn_name = "Player 1"
        else: #player 2's turn
            turn_token = AI
            turn_name = "Player 2"
        
        print(f"{turn_name}'s turn")
        
        #for player 2 we will use the minimax algorithm to pick the best move for the AI player
        if turn_token == AI:
            col, minimax_score = minimax(board, 3, True) #depth 3 (for right now), AI maximizes first
            print(f"AI picks column {col}")
        #human picks move
        else:
            col = int(input("Pick a column (0-6): ")) #get column input

        #validate input and drop token
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_token(board, row, col, turn_token)

            print_board(board)

            #check for win
            if winning_move(board, turn_token):
                print(f"{turn_name} wins!")
                game_over = True

            #check if board is full (AKA a draw)
            if is_board_full(board):
                print("Its a draw!")
                game_over = True
        
            turn += 1 #switch player for next turn
        
        #print if column is full
        else:
            print("Column is full. Pick another column.")
        


#runs game loop if this file is run directly
if __name__ == "__main__":
    game_loop()



    