from chess import based as b
from chess.figures import figures_functions as ff


class Pawn(b.Figure):

    def __init__(self, board, name, color, current_position, is_protected, first_move = True, en_passant_possible = False):
        self.first_move = first_move
        self.en_passant_possible = en_passant_possible
        super().__init__(board, name, color, current_position, is_protected)

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = int(self.current_position[1])

        ff.possible_pawn_moves(self, board, number, letter, asc_letter)

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
