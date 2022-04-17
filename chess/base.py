class Users:

    def __init__(self, name, age, sexual_orientation = 'Gay', score = 0 ):
        pass

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
            
            
    



class Figure:

    def __init__(self, board, name, color, current_position, is_alive = True, is_checking = False):

        self.name = name
        self.color = color
        self.current_position = current_position
        self.possible_moves = []
        self.is_alive = is_alive
        self.is_checking = is_checking
        board.all_figures.append(self)

