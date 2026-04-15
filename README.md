# Artificial-Intelligence-COMP-6600-Final-Project
A Connect Four game with an AI opponent using Minimax with alpha-beta pruning.

---

# Overview
This project implements an AI agent for Connect Four using the Minimax algorithm with alpha-beta pruning. It includes three evaluation heuristics: material count, center control, and threat detection. It also includes two baseline players: random and greedy. This project has an automated experiment runner for empirical comparison. 

---

# Project Structure
```
Artificial-Intelligence-COMP-6600-Final-Project/
├── ai/
│   ├── minimax.py           # Minimax algorithm (with and without alpha-beta pruning)
│   └── heuristics.py        # Evaluation heuristics (material, center, threat)
├── game/
│   ├── board.py             # Board representation and game logic
│   └── game.py              # Interactive game loop
├── players/
│   ├── random_player.py     # Baseline: random legal move
│   ├── greedy_player.py     # Baseline: greedy (wins immediately if possible)
│   ├── minimax_player.py    # AI player using Minimax algorithm
│   └── hint_player.py       # Provides hints to the human player using minimax
├── main.py
├── run_experiments.py       # Automated Experiments
└── README.md
```
--- 

# Running the Interactive Game

To play Connect Four against an AI opponent interactively, run:
`python3 main.py`

You will then be prompted to choose an opponent:
Which AI do you want to play against?
1. greedy
2. random
3. minimax

- Enter `1` or `greedy` to play against the greedy baseline
- Enter `2` or `random` to play against the random baseline
- Enter `3` or `minimax` to play against the minimax baseline

On your turn, enter a column number between 0 and 6 when prompted.
You can also enter `h` at any time to get a hint from the Minimax 
algorithm suggesting the best column to play.

Example:

Enter move (0-6) or 'h' for hint: h

Hint: Try column 3

The board is printed after each move. Row 0 is at the bottom and the tokens fall under gravity. Column numbers are shown along the bottom of the display.

---

# Running Experiments
To reproduce all experimental results, run:
python3 run_experiments.py

This will automatically execute four sets of experiments and print the results to the terminal:

**Experiment 1 - Minimax vs. Random Player**
- 50 games
- Minimax at depth 4
- Reports win rates for each player and average move time

**Experiment 2 - Minimax vs. Greedy Player**
- 50 games
- Minimax at depth 4
- Reports win rates for each player and average move time

**Experiment 3 - Alpha-Beta Pruning vs. No Pruning (Speed Comparison)**
- 10 times trials on an empty board at depth 4
- Reports average computation time with pruning, without pruning, and the speedup factor

**Experiment 4 - Heuristic Weight Comparison**
- Tests four weight configurations `(material, center, threat)` against the random player (50 games each):
    - Threat-heavy (1, 1, 10) - default
    - Balanced (1, 1, 1)
    - Center-heavy (1, 10, 1)
    - Material-heavy (10, 1, 1)
- Reports win rates and average move time for each configuration

---

**Example Output**
```           
Running minimax vs random:
Minimax wins: 50 (100.0%)
Random wins: 0 (0.0%)
Draws: 0
Average move time: 1.0096 seconds

Running minimax vs greedy...
Minimax wins: 50 (100.0%)
Greedy wins: 0 (0.0%)
Draws: 0
Average move time: 0.5903 seconds

Running minimax with alpha-beta pruning vs without alpha-beta pruning:
Average time with alpha-beta: 0.2350 seconds
Average time without alpha-beta: 0.7543 seconds
Speedup from pruning: 3.21x

Running heuristic weight comparisons

Threat heavy vs random - Win rate: 100.0%
Average move time: 0.9360 seconds

Balanced vs random - Win rate: 100.0%
Average move time: 0.9147 seconds

Center heavy vs random - Win rate: 98.0%
Average move time: 1.2380 seconds

Material heavy vs random - Win rate: 100.0%
Average move time: 1.0120 seconds


Threat heavy vs greedy - Win rate: 100.0%
Average move time: 0.5751 seconds

Balanced vs greedy - Win rate: 100.0%
Average move time: 0.6260 seconds

Center heavy vs greedy - Win rate: 100.0%
Average move time: 0.7962 seconds

Material heavy vs greedy - Win rate: 100.0%
Average move time: 0.6128 seconds

Running heuristics against each other
Threat heavy vs Balanced - Threat heavy win rate: 0.0%
Balanced win rate: 100.0%

Threat heavy vs Center heavy - Threat heavy win rate: 0.0%
Center heavy win rate: 100.0%

Threat heavy vs Material heavy - Threat heavy win rate: 0.0%
Material heavy win rate: 100.0%

Balanced vs Center heavy - Balanced win rate: 0.0%
Center heavy win rate: 100.0%

Balanced vs Material heavy - Balanced win rate: 0.0%
Material heavy win rate: 100.0%

Center heavy vs Material heavy - Center heavy win rate: 100.0%
Material heavy win rate: 0.0%
```

_(Exact values will vary slightly because of the randomness in the random player. Timing results will vary by hardware but win rates should be consistent.)_

# Adjusting Experiment Parameters
To change the number of games per experiment, open `run_experiments.py` and edit the `num_games` argument in any `run_experiment(...)` call:
```
results = run_experiment(minimax_player, random_player, num_games=100)
```

To change the Minimax search depth, edit the depth parameter in the lambda definitions:
```
minimax_player = lambda board: minimax(board, 4, True)[0]  # change 4 to desired depth
```
**Note:** Depths above 6 will significantly increase the computation time

---

# Module Descriptions

### `game/board.py`
Core board logic. Defines board dimensions (`ROWS=6`, `COLS=7`), player tokens (`PLAYER=1`, `AI=2`, `EMPTY=0`), and all board operations: `create_board`, `drop_token`, `is_valid_location`, `get_next_open_row`, `winning_move`, `is_board_full`, and `print_board`.

### `game/game.py`
Main game loop. Alternates between the human player and the AI opponent, handles player input, drops tokens, checks for wins and draws, and prints the board after each move.
 
### `ai/heuristics.py`
Three heuristic functions used by the scoring function:
- `material_count(board, player)` — counts open winning lines for each player
- `center_control(board, token)` — weights tokens by column centrality
- `threat_detection(board, token)` — detects 3-in-a-row threats with an open space
 
### `ai/minimax.py`
- `score_board(board, weights)` — combines heuristics into a board score
- `minimax(board, depth, maximizing, alpha, beta, weights)` — minimax with alpha-beta pruning
- `minimax_no_pruning(board, depth, maximizing, weights)` — minimax without pruning (used only in the pruning speed experiment)
 
### `players/random_player.py`
Picks a random valid column on each turn.
 
### `players/greedy_player.py`
Takes a winning move immediately if one exists, otherwise picks the first available column.

### `players/minimax_player.py`
An AI player that uses the Minimax algorithm to evaluate the board and determine 
the best move. Looks ahead a set number of moves (depth=4) and returns 
the column it determines is the best move for the AI.

### `players/hint_player.py`
Provides move hints to the human player using Minimax. Instead of making a move 
itself, it evaluates the board from the human's perspective and suggests the best 
column for the human to play in (depth=4).
 
### `run_experiments.py`
Automated runner for all experiments. Calls `run_experiment(player1, player2, num_games)` to simulate games and collect win rates and timing data.




