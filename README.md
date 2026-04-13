# Artificial-Intelligence-COMP-6600-Final-Project
A Connect Four game with an AI opponent using Minimax with alpha-beta pruning.

# Overview
This project implements an AI agent for Connect Four using the Minimax algorithm with alpha-beta pruning. It includes three evaluation heuristics: material count, center control, and threat detection. It also includes two baseline players: random and greedy. Thi project has an automated experiment runner for empirical comparison. 

# Project Structure
Artificial-Intelligence-COMP-6600-Final-Project/
├── ai/
│   ├── minimax.py           # Minimax algorithm (with and without alpha-beta pruning)
│   └── heuristics.py        # Evaluation heuristics (material, center, threat)
├── experiments/
│   └── run_experiments.py   # Automated Experiment
├── game/
│   ├── board.py             # Board representation and game logic
│   └── game.py              # Interactive game loop
├── players/
│   ├── random_player.py     # Baseline: random legal move
│   └── greedy_player.py     # Baseline: greedy (wins immediately if possible)
├── main.py                   # Entry point for interactive play
└── README.md

# Running the Interactive Game

To play Connect Four against an AI opponent interactively, run:
python main.py

You will then be prompted to choose an opponent:
Which AI do you want to play against?
1. greedy
2. random
3. minimax

- Enter 1 or greedy to play against the greedy baseline
- Enter 2 or random to play against the random baseline
- Enter 3 or minimax to play against the minimax baseline

On your turn, enter a column number between 0 and 6 when prompted.

The board is printed after each move. Row 0 is at the bottom and the tokens fall under gravity. Column numbers are shown along the bottom of the display.

# Running Experiments
To reproduce all experimental results, run:
pythin run_experiments.py

This will automatically execute four sets of experiments and print the results to the terminal:


