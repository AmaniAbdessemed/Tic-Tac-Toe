import copy
import random


class AI:
    def __init__(self, first_player):
        self.player = -1
        self.first_p = first_player
        self.turn = 0

    def minimax(self, board, maximizing):
        # check terminal states :
        result = board.check_win()
        # Human player wins
        if result == 1:
            return 1, None
        # AI player wins
        elif result == -1:
            return -1, None
        # board is full (Tie)
        elif result == 2:
            return 0, None

        if maximizing:
            max_value = -1000
            best_move = None
            empty_squares = board.get_empty_squares()
            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player * -1)
                val = self.minimax(temp_board, False)[0]

                if val > max_value:
                    max_value = val
                    best_move = (row, col)

            return max_value, best_move
        elif not maximizing:
            min_value = 1000
            best_move = None
            empty_squares = board.get_empty_squares()
            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                val = self.minimax(temp_board, True)[0]
                if val < min_value:
                    min_value = val
                    best_move = (row, col)

            return min_value, best_move

    def eval(self, main_board, difficulty):
        if difficulty == 0:
            best_move = self.easy_level(main_board)
            return best_move

        if difficulty == 1:
            if self.turn % 2 == 0:
                best_move = self.hard_level(main_board)
                self.turn += 1
                return best_move
            else:
                best_move = self.easy_level(main_board)
                self.turn += 1
                return best_move

        if difficulty == 2:
            best_move = self.hard_level(main_board)
            return best_move

    def easy_level(self, board):
        empty_squares = board.get_empty_squares()
        index = random.randrange(0, len(empty_squares))
        move = empty_squares[index]
        return move

    def hard_level(self, board):
        if self.first_p != -1:
            val, move = self.minimax(board, False)
            print(f'Ai choose the square :{move} with value of {val}')
            return move
        else:
            move = (1, 1)
            self.first_p += 1
            return move
