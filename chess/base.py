from chess.figures.Pawn import Pawn
from chess.figures.Bishop import Bishop
from chess.figures.Knight import Knight
from chess.figures.Rook import Rook
from chess.figures.Queen import Queen
from chess.figures.King import King
from chess.utils import change_turn, check_for_mate, check_for_stalemate, check_the_turn, register_user, action



class Users:

    def __init__(self, name = '', age = 0, sexual_orientation = 'Gay', score = 0, color = '', my_turn = False):
        self.name = name
        self.age = age
        self.sexual_orientation = sexual_orientation
        self.score = score
        self.color = color
        self.my_turn = my_turn

class Board:

    all_figures = []
    taken_squares = []
    all_squares = []
    def __init__(self):
        for i in range(1, 9, 1):
            for x in range(97, 106, 1):
                letter = chr(x)
                number = i
                self.all_squares.append(f'{letter} + {number}')

    def check_taken_squares(self):
        self.taken_squares = []
        for figure in self.all_figures:
            if figure.is_alive == True:
                self.taken_squares.append(figure.current_position)

    def check_all_figures(self):
        for figure in self.all_figures:
            if figure.is_alive != True:
                self.all_figures.remove(figure)

    def refresh(self):
        self.check_all_figures()
        self.check_taken_squares()
            
            
    



class Figure:

    def __init__(self, board, name, color, current_position, is_protected, is_alive = True, is_checking = False):

        self.name = name
        self.color = color
        self.current_position = current_position
        self.possible_moves = []
        self.is_alive = is_alive
        self.is_checking = is_checking
        self.is_protected = is_protected
        board.all_figures.append(self)



class Game:

    moves = {}
    board = Board()

    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    a2Pawn = Pawn(board, 'pa2', 'w', 'a2', is_protected = True)
    b2Pawn = Pawn(board, 'pb2', 'w', 'b2', is_protected = True)
    c2Pawn = Pawn(board, 'pc2', 'w', 'c2', is_protected = True)
    d2Pawn = Pawn(board, 'pd2', 'w', 'd2', is_protected = True)
    e2Pawn = Pawn(board, 'pe2', 'w', 'e2', is_protected = True)
    f2Pawn = Pawn(board, 'pf2', 'w', 'f2', is_protected = True)
    g2Pawn = Pawn(board, 'pg2', 'w', 'g2', is_protected = True)
    h2Pawn = Pawn(board, 'ph2', 'w', 'h2', is_protected = True)
    a1Rook = Rook(board, 'Ra1', 'w', 'a1', is_protected = False)
    h1Rook = Rook(board, 'Rh1', 'w', 'h1', is_protected = False)
    b1Knight = Knight(board, 'Nb1', 'w', 'b1', is_protected = True)
    g1Knight = Knight(board, 'Ng1', 'w', 'g1', is_protected = True)
    c1Bishop = Bishop(board, 'Bc1', 'w', 'c1', is_protected = True)
    f1Bishop = Bishop(board, 'Bf1', 'w', 'f1', is_protected = True)
    d1Queen = Queen(board, 'Qd1', 'w', 'd1', is_protected = True)
    e1King = King(board, 'Ke1', 'w', 'e1', is_protected = True)

    a7Pawn = Pawn(board, 'pa7', 'b', 'a7', is_protected = True)
    b7Pawn = Pawn(board, 'pb7', 'b', 'b7', is_protected = True)
    c7Pawn = Pawn(board, 'pc7', 'b', 'c7', is_protected = True)
    d7Pawn = Pawn(board, 'pd7', 'b', 'd7', is_protected = True)
    e7Pawn = Pawn(board, 'pe7', 'b', 'e7', is_protected = True)
    f7Pawn = Pawn(board, 'pf7', 'b', 'f7', is_protected = True)
    g7Pawn = Pawn(board, 'pg7', 'b', 'g7', is_protected = True)
    h7Pawn = Pawn(board, 'ph7', 'b', 'h7', is_protected = True)
    a8Rook = Rook(board, 'Ra8', 'b', 'a8', is_protected = False)
    h8Rook = Rook(board, 'Rh8', 'b', 'h8', is_protected = False)
    b8Knight = Knight(board, 'Nb8', 'b', 'b8', is_protected = True)
    g8Knight = Knight(board, 'Ng8', 'b', 'g8', is_protected = True)
    c8Bishop = Bishop(board, 'Bc8', 'b', 'c8', is_protected = True)
    f8Bishop = Bishop(board, 'Bf8', 'b', 'f8', is_protected = True)
    d8Queen = Queen(board, 'Qd8', 'b', 'd8', is_protected = True)
    e8King = King(board, 'Ke8', 'b', 'e8', is_protected = True)

    def play(self):
        turn = 0
        while check_for_mate(self.e8king) and check_for_stalemate(self.e1King):
            self.board.refresh()
            turner = check_the_turn(self.user1, self.user2)
            move = action(turner, self.board)

            change_turn(self.user1, self.user2)
            turn += 1

            if turn % 2 != 0:
                self.moves[str(turn)].append(move)
            else:
                self.moves[str(turn-1)].append(move)
        new_game_mb = input('Would you like to start a new game?\n')
        return new_game_mb
