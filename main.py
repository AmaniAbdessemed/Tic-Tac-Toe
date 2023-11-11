import pygame, sys

from GAME import Game
from BUTTON import Button
from constants import *

# pygame setup
pygame.init()

# set the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
screen.fill(BG_COLOR)

font = pygame.font.SysFont('arialblack', 40)
text_color = (99, 74, 194)

human_img = pygame.image.load("assets/Human.png")
ai_img = pygame.image.load("assets/Ai.png")

start_img = pygame.image.load("assets/Start.png")
start_btn = Button(WIDTH // 2 - 100, HEIGHT - 180, start_img, 1.1)

easy_img = pygame.image.load("assets/Easy.png")
med_img = pygame.image.load("assets/med.png")
hard_img = pygame.image.load("assets/Hard.png")

restart_img = pygame.image.load("assets/replay.png")
restart_btn = Button(WIDTH - 200, HEIGHT - 100, restart_img, 1.1)

back_img = pygame.image.load("assets/Back.png")
back_btn = Button(100, HEIGHT - 100, back_img, 1.1)


def mode():
    hello_txt = font.render("Welcome to the game!", True, LINE_COLOR)
    first_txt = font.render("Choose your starting player.", True, LINE_COLOR)
    diff_txt = font.render("Choose the difficulty level.", True, LINE_COLOR)

    pygame.display.set_caption("Options")
    screen.fill(BG_COLOR)

    level_btn = Button(WIDTH // 2 - 80, HEIGHT - 350, hard_img, 1.2)
    first_p_btn = Button(WIDTH // 2 - 100, HEIGHT - 550, human_img, 1.2)

    # difficulty level easy = 0, medium = 1 and hard = 2
    level = 2
    # AI or human
    first_player = 1

    while True:
        screen.blit(hello_txt, (WIDTH // 2 - hello_txt.get_width() // 2,
                                HEIGHT - 700 - hello_txt.get_height() // 2))
        screen.blit(first_txt, (WIDTH // 2 - first_txt.get_width() // 2,
                                HEIGHT - 600 - first_txt.get_height() // 2))
        screen.blit(diff_txt, (WIDTH // 2 - diff_txt.get_width() // 2,
                               HEIGHT - 400 - diff_txt.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if level_btn.draw(screen):
                if level == 2:
                    level_btn = Button(WIDTH // 2 - 80, HEIGHT - 350, easy_img, 1.2)
                    level = 0
                elif level == 1:
                    level_btn = Button(WIDTH // 2 - 80, HEIGHT - 350, hard_img, 1.2)
                    level = 2
                else:
                    level_btn = Button(WIDTH // 2 - 80, HEIGHT - 350, med_img, 1.2)
                    level = 1

            if first_p_btn.draw(screen):
                if first_player == 1:
                    first_p_btn = Button(WIDTH // 2 - 100, HEIGHT - 550, ai_img, 1.2)
                else:
                    first_p_btn = Button(WIDTH // 2 - 100, HEIGHT - 550, human_img, 1.2)
                first_player *= -1

            if start_btn.draw(screen):
                start(level, first_player)

        pygame.display.update()


def start(diff_level, first_player):
    screen.fill(BG_COLOR)
    game = Game(screen, first_player)
    board = game.board
    ai = game.ai
    test = True
    while game.running or test:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and game.player == 1:
                print(event)
                x = event.pos[0] - 60
                y = event.pos[1] - 10
                clicked_row = y // SQUARE
                clicked_col = x // SQUARE
                if not (clicked_row >= 3 or clicked_col >= 3):
                    print(clicked_row, clicked_col)
                    if game.board.available_square(clicked_row, clicked_col) and game.running:
                        game.make_move(clicked_row, clicked_col)
                        if game.game_over():
                            game.running = False
            if game.player == -1 and game.running:
                pygame.display.update()
                row, col = ai.eval(board, diff_level)
                game.make_move(row, col)
                if game.game_over():
                    game.running = False

            if back_btn.draw(screen):
                mode()
            # print("winner is :", game.board.check_win())

            if restart_btn.draw(screen):
                screen.fill(BG_COLOR)
                game.restart()
                board = game.board
                ai = game.ai

            # to update the screen
            pygame.display.update()
            clock.tick(60)


mode()
