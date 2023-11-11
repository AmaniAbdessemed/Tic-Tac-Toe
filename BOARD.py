import numpy

class Board:
    def __init__(self):
        self.board = numpy.zeros((3, 3))
        self.win_pos = 0, '-'

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def full_board(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False
        return True

    def get_empty_squares(self):
        empty_squares = []
        for row in range(3):
            for col in range(3):
                if self.available_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares

    def check_win(self, show=False):
        # horizontal winning lines
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                if show:
                    self.win_pos = self.board[row][0], row, 'row'
                return self.board[row][0]

        # vertical winning lines
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                if show:
                    self.win_pos = self.board[0][col], col, 'col'
                return self.board[0][col]

        # diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            if show:
                self.win_pos = self.board[0][0], 0, 'dia'
            return self.board[0][0]

        # anti diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            if show:
                self.win_pos = self.board[0][2], 0, 'a-dia'
            return self.board[0][2]

        # tie/draw
        if self.full_board():
            if show:
                self.win_pos = 2, 3, 'tie'
            return 2
        return 0

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col])

