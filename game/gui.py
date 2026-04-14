import pygame
import sys
from game.board import *

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5

width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE

#pygame.init()
screen = pygame.display.set_mode((width, height))

def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE,
                (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            
            pygame.draw.circle(screen, BLACK,
                (int(c*SQUARESIZE + SQUARESIZE/2),
                 int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == PLAYER:
                pygame.draw.circle(screen, RED,
                    (int(c*SQUARESIZE + SQUARESIZE/2),
                     height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)

            elif board[r][c] == AI:
                pygame.draw.circle(screen, YELLOW,
                    (int(c*SQUARESIZE + SQUARESIZE/2),
                     height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    pygame.display.update()

def gui_game_loop(ai_player):
    board = create_board()
    draw_board(board)

    game_over = False
    turn = 0

    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # HUMAN MOVE
            if turn % 2 == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // SQUARESIZE

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_token(board, row, col, PLAYER)

                        if winning_move(board, PLAYER):
                            print("Player wins!")
                            game_over = True

                        turn += 1
                        draw_board(board)

        # AI MOVE (outside event loop)
        if turn % 2 == 1 and not game_over:
            col = ai_player(board)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_token(board, row, col, AI)

                if winning_move(board, AI):
                    print("AI wins!")
                    game_over = True

                turn += 1
                draw_board(board)

#font = pygame.font.SysFont("monospace", 75)
#label = font.render("Player wins!", True, RED)
#screen.blit(label, (40, 10))
#pygame.display.update()
#
#pygame.time.wait(500)