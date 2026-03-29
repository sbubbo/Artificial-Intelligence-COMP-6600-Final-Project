"""
This file sets up the Connect Four game and loop

Functions of this file include: 
 - game_loop: alternates between player 1 and player 2 picking a column to drop their token, 
              then checking for a win until someone wins or the board is full
"""

#import everything from board.py
from game.board import *

from players.greedy_player import greedy_player
from players.random_player import random_player

#main game loop. takes the ai as an argument so that we can use different ai players if we want to
def game_loop(which_ai):
    board = create_board() #fresh board at the start of game
    print_board(board)

    game_over = False
    turn = 0 #player 1 goes first

    while not game_over: #continues to loop as long as no one has one and board is not full
        if turn % 2 == 0: #player 1's turn
            turn_token = PLAYER
            turn_name = "Player 1"
            col = int(input("Pick a column (0-6): ")) #get column input
        
        else: #AI's turn
            turn_token = AI
            turn_name = "Player 2"
            col = which_ai(board) #let the AI pick a column

        print(f"{turn_name}'s turn")

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
    which_ai = input("Which AI do you want to play against? \n1. greedy\n2. random\n3. minimax\n")
    if which_ai == "greedy" or which_ai == "1":
        game_loop(greedy_player)
    elif which_ai == "random" or which_ai == "2":
        game_loop(random_player)
    elif which_ai == "minimax" or which_ai == "3":
        from ai.minimax import minimax
        game_loop(lambda board: minimax(board, 6, True)[0]) #use a lambda to call minimax with the right arguments and only return the column
    else:
        print("Invalid input, defaulting to random player")
        game_loop(random_player)
