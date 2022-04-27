from chess.base import Figure
from chess.figures.figures_functions import checking_squares_for_knight

class Knight(Figure):

    def __init__():
        pass

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = self.current_position[1]

        for x in range(-2, 4, 2):
            xnumber = number + x
            xletter = asc_letter + x
            checking_squares_for_knight(self, number, asc_letter, xnumber, xletter, board.all_squares)


    def move(self, new_position):
        if (self.is_alive == True) and new_position in self.possible_moves:
            self.current_position = new_position
        else:
            print('This move is not possible. Please enter something sane')

    def take(self, new_position, other_piece):
        if (self.is_alive == True) and new_position in self.possible_moves:
            self.current_position = new_position
            other_piece.is_alive = False
        else:
            print('This move is not possible. Please enter something sane')