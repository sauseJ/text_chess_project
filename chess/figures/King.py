from chess.figures.figures_functions import castle_kingside, castle_queenside, checking_squares_for_king
from base import Figure

class King(Figure):

    def __init__(self, first_move = True, in_check = False):
        self.first_move = first_move
        self.in_check = in_check

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = self.current_position[1]

        checking_squares_for_king(self, board, number, asc_letter)
        

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

    def short_castle(self, board):
        castle_kingside(self, board)

    def long_castle(self, board):
        castle_queenside(self, board)