from figures_functions import find_figure_by_position
from base import Figure

class Pawn(Figure):

    def __init__(self, first_move = True, en_passant_possible = False):
        self.first_move = first_move
        self.en_passant_possible = en_passant_possible

    def check_possible_moves(self, board):
        self.possible_moves = []
        letter = self.current_position[0]
        asc_letter = ord(letter)
        number = self.current_position[1]

        if (self.color == 'w') and (self.first_move == True):
            for i in range(2, 0, -1):
                new_number = number + i
                possible_move = f'{letter} + {new_number}'

                if (possible_move) not in board.taken_squares:
                    self.possible_moves.append(possible_move)


        if (self.color == 'w') and (self.first_move == False):
            new_number = number + 1
            possible_move = f'{letter} + {new_number}'

            if possible_move not in board.taken_squares:
                self.possible_moves.append(possible_move)

        
        if self.color == 'w':
            new_number = number + 1
            for i in range(-1, 3, 2):
                new_letter = chr(asc_letter + i)
                possible_move = f'{new_letter} + {new_number}'
                french_move = f'{new_letter} + {number}'

                side_figure = (find_figure_by_position(board.all_figures, french_move))
                if ('en_passant_possible' in dir(side_figure)):
                    french_pawn = side_figure
                other_figure = find_figure_by_position(board.all_figures, possible_move)

                if ((possible_move in board.taken_squares) and (other_figure.color != 'w'))\
                or\
                ((possible_move not in board.taken_squares) and (french_pawn.color != 'w') and (french_pawn.en_passant_possible == True)):
                    self.possible_moves.append(possible_move)


        if (self.color == 'b') and (self.first_move == True):
            for i in range(2, 0, -1):
                new_number = number - i
                possible_move = f'{letter} + {new_number}'

                if (possible_move) not in board.taken_squares:
                    self.possible_moves.append(possible_move)


        if (self.color == 'b') and (self.first_move == False):
            new_number = number - 1
            possible_move = f'{letter} + {new_number}'

            if possible_move not in board.taken_squares:
                self.possible_moves.append(possible_move)

        
        if self.color == 'b':
            new_number = number - 1
            for i in range(-1, 3, 2):
                new_letter = chr(asc_letter + i)
                possible_move = f'{new_letter} + {new_number}'
                french_move = f'{new_letter} + {number}'

                side_figure = (find_figure_by_position(board.all_figures, french_move))
                if ('en_passant_possible' in dir(side_figure)):
                    french_pawn = side_figure
                other_figure = find_figure_by_position(board.all_figures, possible_move)

                if ((possible_move in board.taken_squares) and (other_figure.color != 'b'))\
                or\
                ((possible_move not in board.taken_squares) and (french_pawn.color != 'b') and (french_pawn.en_passant_possible == True)):
                    self.possible_moves.append(possible_move)
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????
# BITCH YOU BETTER NOT FORGET THAT THESE PIECES OF SHIT CAN TRANSFORM DO YOU HEAR ME??????????        

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
