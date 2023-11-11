from BOARD import Board
from AI import AI
import pygame
from constants import *

ORG_BOARD = pygame.image.load("assets/Board.png")
BOARD = pygame.transform.scale(ORG_BOARD, (660, 660))
X_IMG = pygame.image.load("assets/X.png")
ORG_O_IMG = pygame.image.load("assets/O.png")
O_IMG = pygame.transform.scale(ORG_O_IMG, (160, 160))


class Game:
    def __init__(self, screen, first_player):
        self.board = Board()
        self.first_player = first_player
        self.player = first_player
        self.ai = AI(first_player)
        screen.blit(BOARD, (50, 10))
        self.screen = screen
        self.running = True

    def next_turn(self):
        self.player *= -1

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw(col * SQUARE + 80, row * SQUARE + 40, self.player)
        self.next_turn()

    def draw(self, row, col, player):
        if player == 1:
            self.screen.blit(X_IMG, (row, col))
        else:
            self.screen.blit(O_IMG, (row, col))

    def draw_win_line(self, pos):
        color = O_COLOR if pos[0] == -1 else X_COLOR
        if pos[2] == 'row':
            ipos = (20, pos[1] * SQUARE + SQUARE // 2)
            fpos = (WIDTH - 20, pos[1] * SQUARE + SQUARE // 2)
            pygame.draw.line(self.screen, color, ipos, fpos, 15)
        if pos[2] == 'col':
            ipos = (pos[1] * SQUARE + 40 + SQUARE // 2, 20)
            fpos = (pos[1] * SQUARE + 40 + SQUARE // 2, HEIGHT - 100)
            pygame.draw.line(self.screen, color, ipos, fpos, 15)
        if pos[2] == 'dia':
            ipos = (80, 40)
            fpos = (WIDTH - 40, HEIGHT - 80)
            pygame.draw.line(self.screen, color, ipos, fpos, 15)
        if pos[2] == 'a-dia':
            ipos = (WIDTH - 90, 20)
            fpos = (40, HEIGHT - 100)
            pygame.draw.line(self.screen, color, ipos, fpos, 15)

    def game_over(self):
        result = self.board.check_win(True)
        if result == -1 or result == 1:
            self.draw_win_line(self.board.win_pos)
            return True
        if self.board.full_board():
            return True
        else:
            return False

    def restart(self):
        self.__init__(self.screen, self.first_player)
