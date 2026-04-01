"""
This file is to set up experiments that will automatically run between different AI players to collect data

Functions of this file include: 
 - run_experiment: runs a specified number of games between two AI players and collects data on wins, losses, and draws
 - run_matchups: runs a series of experiments between different AI players to compare their performance
"""

#import
import time
from game.board import *
from ai.minimax import minimax
from players.random_player import random_player
from players.greedy_player import greedy_player

def run_experiment(player1, player2, num_games = 50):
    #track results 
    results = {"player1_wins": 0, "player2_wins": 0, "draws": 0} #player 1 and player 2 are the two AI players being compared
    total_time = 0

    for game in range(num_games): #runs game N times (N = 50 here)
        board = create_board() #create a new game board for each game
        game_over = False
        turn = 0 #player 1 goes first

        while not game_over:
            if turn % 2 == 0:
                turn_token = PLAYER
                start = time.time()
                col = player1(board) #get move from player 1
                total_time += time.time() - start #measures how long each move takes and adds to total
            else:
                turn_token = AI
                start = time.time()
                col = player2(board) #get move from player 2
                total_time += time.time() - start 

            #drop the token and check for wins
            if col is not None and is_valid_location(board, col): #if move is valid
                row = get_next_open_row(board, col)
                drop_token(board, row, col, turn_token) #make move

                if winning_move(board, turn_token): #check if move wins game
                    if turn % 2 == 0:
                        results["player1_wins"] += 1
                    else:
                        results["player2_wins"] += 1
                    game_over = True
                elif is_board_full(board): #check for draw
                    results["draws"] += 1
                    game_over = True
                
                turn += 1 #switch turns

    average_time = total_time / (num_games)

    #return the results
    return {
        "player1_wins": results["player1_wins"],
        "player2_wins": results["player2_wins"],
        "draws": results["draws"],
        "win_rate_player1": results["player1_wins"] / num_games * 100,
        "win_rate_player2": results["player2_wins"] / num_games * 100,
        "average_move_time": average_time
    }

def run_matchups():
    #set up minimax player as a lamba so it matches the same format as other players
    minimax_player = lambda board: minimax(board, 4, True) [0] #depth of 4

    #minimax v random
    #prints results of experiments including win rates and average move time
    print("Running minimax vs random:")
    results = run_experiment(minimax_player, random_player)
    print(f"Minimax wins: {results['player1_wins']} ({results['win_rate_player1']:.1f}%)")
    print(f"Random wins: {results['player2_wins']} ({results['win_rate_player2']:.1f}%)")
    print(f"Draws: {results['draws']}")
    print(f"Average move time: {results['average_move_time']:.4f} seconds")
    print()
    
    # run minimax vs greedy
    print("Running minimax vs greedy...")
    results = run_experiment(minimax_player, greedy_player)
    print(f"Minimax wins: {results['player1_wins']} ({results['win_rate_player1']:.1f}%)")
    print(f"Greedy wins: {results['player2_wins']} ({results['win_rate_player2']:.1f}%)")
    print(f"Draws: {results['draws']}")
    print(f"Average move time: {results['average_move_time']:.4f} seconds")
    print()

    #minimax vs minimax without alpha-beta (to prove pruning works)
    print("Running minimax with alpha-beta vs without alpha-beta...")
    minimax_no_pruning = lambda board: minimax(board, 4, True, -100000000, 100000000)[0]
    results = run_experiment(minimax_player, minimax_no_pruning, num_games=50)
    print(f"With alpha-beta wins: {results['player1_wins']} ({results['win_rate_player1']:.1f}%)")
    print(f"Without alpha-beta wins: {results['player2_wins']} ({results['win_rate_player2']:.1f}%)")
    print(f"Draws: {results['draws']}")
    print(f"Average move time: {results['average_move_time']:.4f} seconds")
    print()

    """
This file is to set up experiments that will automatically run between different AI players to collect data

Functions of this file include: 
 - run_experiment: runs a specified number of games between two AI players and collects data on wins, losses, and draws
 - run_matchups: runs a series of experiments between different AI players to compare their performance
"""

#import
import time
from game.board import *
from ai.minimax import minimax
from players.random_player import random_player
from players.greedy_player import greedy_player

def run_experiment(player1, player2, num_games = 50):
    #track results 
    results = {"player1_wins": 0, "player2_wins": 0, "draws": 0} #player 1 and player 2 are the two AI players being compared
    total_time = 0

    for game in range(num_games): #runs game N times (N = 50 here)
        board = create_board() #create a new game board for each game
        game_over = False
        turn = 0 #player 1 goes first

        while not game_over:
            if turn % 2 == 0:
                turn_token = PLAYER
                start = time.time()
                col = player1(board) #get move from player 1
                total_time += time.time() - start #measures how long each move takes and adds to total
            else:
                turn_token = AI
                start = time.time()
                col = player2(board) #get move from player 2
                total_time += time.time() - start 

            #drop the token and check for wins
            if col is not None and is_valid_location(board, col): #if move is valid
                row = get_next_open_row(board, col)
                drop_token(board, row, col, turn_token) #make move

                if winning_move(board, turn_token): #check if move wins game
                    if turn % 2 == 0:
                        results["player1_wins"] += 1
                    else:
                        results["player2_wins"] += 1
                    game_over = True
                elif is_board_full(board): #check for draw
                    results["draws"] += 1
                    game_over = True
                
                turn += 1 #switch turns

    average_time = total_time / (num_games)

    #return the results
    return {
        "player1_wins": results["player1_wins"],
        "player2_wins": results["player2_wins"],
        "draws": results["draws"],
        "win_rate_player1": results["player1_wins"] / num_games * 100,
        "win_rate_player2": results["player2_wins"] / num_games * 100,
        "average_move_time": average_time
    }

def run_matchups():
    #set up minimax player as a lamba so it matches the same format as other players
    minimax_player = lambda board: minimax(board, 4, True) [0] #depth of 4

    #minimax v random
    #prints results of experiments including win rates and average move time
    print("Running minimax vs random:")
    results = run_experiment(minimax_player, random_player)
    print(f"Minimax wins: {results['player1_wins']} ({results['win_rate_player1']:.1f}%)")
    print(f"Random wins: {results['player2_wins']} ({results['win_rate_player2']:.1f}%)")
    print(f"Draws: {results['draws']}")
    print(f"Average move time: {results['average_move_time']:.4f} seconds")
    print()
    
    # run minimax vs greedy
    print("Running minimax vs greedy:")
    results = run_experiment(minimax_player, greedy_player)
    print(f"Minimax wins: {results['player1_wins']} ({results['win_rate_player1']:.1f}%)")
    print(f"Greedy wins: {results['player2_wins']} ({results['win_rate_player2']:.1f}%)")
    print(f"Draws: {results['draws']}")
    print(f"Average move time: {results['average_move_time']:.4f} seconds")
    print()

    #minimax vs minimax without alpha-beta (to prove pruning works)
    print("Running minimax with alpha-beta vs without alpha-beta:")
    import time
    test_board = create_board()
    
    start = time.time()
    for _ in range(10):
        minimax(test_board, 4, True)
    with_pruning = (time.time() - start) / 10
    
    start = time.time()
    for _ in range(10):
        minimax(test_board, 4, True, -100000000, 100000000)
    without_pruning = (time.time() - start) / 10
    
    print(f"Average time with alpha-beta: {with_pruning:.4f} seconds")
    print(f"Average time without alpha-beta: {without_pruning:.4f} seconds")
    print()

if __name__ == "__main__":
    run_matchups()

# heuristic weight comparisons
    print("Running heuristic weight comparisons...")
    
    threat_heavy = lambda board: minimax(board, 4, True, weights=(1, 1, 10))[0]
    balanced = lambda board: minimax(board, 4, True, weights=(1, 1, 1))[0]
    center_heavy = lambda board: minimax(board, 4, True, weights=(1, 10, 1))[0]
    material_heavy = lambda board: minimax(board, 4, True, weights=(10, 1, 1))[0]
    
    for name, player in [("Threat heavy", threat_heavy), ("Balanced", balanced), 
                          ("Center heavy", center_heavy), ("Material heavy", material_heavy)]:
        results = run_experiment(player, random_player, num_games=50)
        print(f"{name} vs random - Win rate: {results['win_rate_player1']:.1f}%")

if __name__ == "__main__":
    run_matchups()

