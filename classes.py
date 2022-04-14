




class Users:

    def __init__(self, name, age, sexual_orientation = 'Gay', score = 0 ):
        pass

class Board:

    all_figures = []
    taken_squares = []
    all_squares = []
    def __init__(self) -> None:
        for i in range(1, 9, 1):
            for x in range(97, 106, 1):
                letter = chr(x)
                number = i
                self.all_squares.append(f'{letter} + {number}')

    def check_taken_squares(self):
        self.taken_squares = []
        for figure in self.all_figures:
            self.taken_squares.append(figure.current_position)
            
            
    

class Pawn:

    def __init__(self, board, name, color, current_position, first_move = True, en_passant_possible = False, is_alive = True):

        self.name = name
        self.color = color
        self.current_position = current_position
        self.possible_moves = []
        self.first_move = first_move
        self.en_passant_possible = en_passant_possible
        self.is_alive = is_alive
        board.all_figures.append(self)

    def calculate_possible_moves(self, board):
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = self.current_position[1]

        if (self.color == 'w') and (self.first_move == True):
            for i in range(2, 0, -1):
                new_number = number + i
                if (f'{letter} + {new_number}') not in board.taken_squares:
                    self.possible_moves.append(f'{letter} + {new_number}')

        if (self.color == 'w') and (self.first_move == False):
            new_number = number + 1
            if (f'{letter} + {new_number}') not in board.taken_squares:
                self.possible_moves.append(f'{letter} + {new_number}')
            
        

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

class Bishop:
    pass

class Knight:
    pass

class Rook:
    pass

class Queen:
    pass

class King:
    pass

class Game:
    
    def __init__(self) -> None:
        pass
    pass