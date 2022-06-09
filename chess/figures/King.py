from chess.figures import figures_functions as ff
from chess import based as b
from chess.figures import Rook


class King(b.Figure):

    def __init__(self, board, name, color, current_position, is_protected, first_move = True, in_check = False):
        self.first_move = first_move
        self.in_check = in_check
        super().__init__(board, name, color, current_position, is_protected)

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = int(self.current_position[1])

        ff.checking_squares_for_king(self, board, number, asc_letter)
        

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
    
    def am_i_in_check(self, board):
        c = 0

        for figure in board.all_figures:
            if (self.current_position in figure.possible_moves) and (figure.color != self.color):
                c += 1

        if c > 0:
            self.in_check = True
        if c == 0:
            self.in_check = False
        

    def short_castle(self, board, wattackers = 0, battackers = 0):
        if (self.first_move == True) and (self.in_check == False):
            if self.color == 'w':
                rook = ff.find_figure_by_position(board.all_figures, 'h1')
                if (type(rook) == Rook.Rook) and (rook.color == 'w') and (rook.first_move == True)\
                and (('f1' and 'g1') not in board.taken_squares):
                    for figure in board.all_figures:
                        if ('f1' or 'g1') in figure.possible_moves and figure.color != 'w':
                            wattackers +=1
                    if wattackers == 0:
                        self.current_position = 'g1'
                        rook.current_position = 'f1'
                    else:
                        raise IndexError("You cannot castle kingside")
                else:
                    raise IndexError("You cannot castle kingside")
                    
        if self.color == 'b':
                rook = ff.find_figure_by_position(board.all_figures, 'h8')
                if (type(rook) == Rook.Rook) and (rook.color == 'b') and (rook.first_move == True)\
                and (('f8' and 'g8') not in board.taken_squares):
                    for figure in board.all_figures:
                        if ('f8' or 'g8') in figure.possible_moves and figure.color != 'b':
                            battackers +=1
                    if battackers == 0:
                        self.current_position = 'g8'
                        rook.current_position = 'f8'
                    else:
                        raise IndexError("You cannot castle kingside")
                else:
                    raise IndexError("You cannot castle kingside")

    def long_castle(self, board, wattackers = 0, battackers = 0):
        if (self.first_move == True) and (self.in_check == False):
            if self.color == 'w':
                rook = ff.find_figure_by_position(board.all_figures, 'a1')
                if (type(rook) == Rook.Rook) and (rook.color == 'w') and (rook.first_move == True)\
                and (('b1' and 'c1' and 'd1') not in board.taken_squares):
                    for figure in board.all_figures:
                        if ('b1' or 'c1' or 'd1') in figure.possible_moves and figure.color != 'w':
                            wattackers +=1
                    if wattackers == 0:
                        self.current_position = 'c1'
                        rook.current_position = 'd1'
                    else:
                        raise IndexError("You cannot castle queenside")
                else:
                    raise IndexError("You cannot castle queenside") 

            if self.color == 'b':
                rook = ff.find_figure_by_position(board.all_figures, 'a8')
                if (type(rook) == Rook.Rook) and (rook.color == 'b') and (rook.first_move == True)\
                and (('b8' and 'c8' and 'd8') not in board.taken_squares):
                    for figure in board.all_figures:
                        if ('b8' or 'c8' or 'd8') in figure.possible_moves and figure.color != 'b':
                            battackers +=1
                    if battackers == 0:
                        self.current_position = 'c8'
                        rook.current_position = 'd8'
                    else:
                        raise IndexError("You cannot castle queenside")
                else:
                    raise IndexError("You cannot castle queenside")