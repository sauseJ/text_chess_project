from chess.figures.figures_functions import possible_pawn_moves
from chess.base import Figure

class Pawn(Figure):

    def __init__(self, first_move = True, en_passant_possible = False):
        self.first_move = first_move
        self.en_passant_possible = en_passant_possible

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = self.current_position[1]

        possible_pawn_moves(self, board, number, letter, asc_letter)

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
