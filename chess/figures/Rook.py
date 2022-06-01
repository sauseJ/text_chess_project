from chess import based as b
from chess.figures import figures_functions as ff

class Rook(b.Figure):

    def __init__(self, board, name, color, current_position, is_protected, first_move=True):
        self.first_move = first_move
        super().__init__(board, name, color, current_position, is_protected)        
        
        
    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = int(self.current_position[1])

        leap_u = 0
        leap_d = 0
        leap_l = 0
        leap_r = 0

        for x in range(1, 8, 1):
            up_number = number + x
            down_number = number - x
            up_letter = asc_letter + x
            down_letter = asc_letter - x
            leap_u, leap_d, leap_l, leap_r = ff.checking_all_sides(self, board, asc_letter, number, up_number, down_number, up_letter, down_letter, board.all_squares, leap_u, leap_d, leap_l, leap_r)


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
