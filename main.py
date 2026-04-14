"""
main.py
"""

from game.game import game_loop
from players.greedy_player import greedy_player
from players.random_player import random_player
from players.minimax_player import minimax_player
#from game.gui import gui_game_loop


if __name__ == "__main__":
    which_ai = input("Which AI do you want to play against? \n1. greedy\n2. random\n3. minimax\n")
    if which_ai == "greedy" or which_ai == "1":
        #hint = input("Would you like a hint system? (y/n)\n") 
        game_loop(greedy_player)
    elif which_ai == "random" or which_ai == "2":
        game_loop(random_player)
    elif which_ai == "minimax" or which_ai == "3":
        game_loop(minimax_player)
    else:
        print("Invalid input, defaulting to random player")
        game_loop(random_player)