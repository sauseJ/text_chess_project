import random
from chess.figures.figures_functions import find_figure_by_position, find_figure_by_possible_move, find_my_king, pawn_promotion
from chess.figures.Pawn import Pawn
from chess.figures.Bishop import Bishop
from chess.figures.Knight import Knight
from chess.figures.Rook import Rook
from chess.figures.Queen import Queen
from chess.figures.King import King


def register_user(user):
    user.name = input('Stage your name: ')
    user.age = input('Stage your age too: ')
    user.sexual_orientation = input('Are you gay or something? ')
    print('Enjoy terminal chess!')

def random_side(user1, user2):
    i = random.randint(0, 1)
    if i == 1:
        user1.color = 'w'
        user1.my_turn = True
        user2.color = 'b'
        user2.my_turn = False
        print(f'Looks like it\'s {user1.name}\'s turn to move now!')
    else:
        user1.color = 'b'
        user1.my_turn = False
        user2.color = 'w'
        user2.my_turn = True
        print(f'Looks like it\'s {user2.name}\'s turn to move now!')

def figure_check(move, board, user):
    letter = move[0]
    if letter == 'B':
        bishop = find_figure_by_possible_move(board.all_figures, move, Bishop, user)
        return bishop
    if letter == 'N':
        knight = find_figure_by_possible_move(board.all_figures, move, Knight, user)
        return knight
    if letter == 'R':
        rook = find_figure_by_possible_move(board.all_figures, move, Rook, user)
        return rook
    if letter == 'Q':
        queen = find_figure_by_possible_move(board.all_figures, move, Queen, user)
        return queen
    if letter == 'K':
        king = find_figure_by_possible_move(board.all_figures, move, King, user)
        return king
    if letter in ['a','b','c','d','e','f','g','h']:
        pawn = find_figure_by_possible_move(board.all_figures, move, Pawn, user)
        if '=' in move:
            new_figure = pawn_promotion(pawn, board, move)
            return new_figure
        else:
            return pawn
        


def action(user, board):
    move = input(f'{user.name}, what\'s your move then: ')
    if move == ('O-O' or '0-0'):
        find_my_king(user, board).short_castle()
    elif move == ('O-O-O' or '0-0-0'):
        find_my_king(user, board).long_castle()
    else:
        figure = figure_check(move, board)

        if 'x' in move:
            opponent_figure = find_figure_by_position(board.all_figures, move[-2:])
            figure.take(move[-2:], opponent_figure)
        else:
            figure.move(move[-2:])
    return move

def check_for_stalemate(king):
    if (king.possible_moves == False) and (king.in_check == False):
        return True

def check_for_mate(king):
    if (king.possible_moves == False) and (king.in_check == True):
        return True

def check_the_turn(user1, user2):
    if user1.my_turn:
        return user1
    else:
        return user2

def change_turn(user1, user2):
    if user1.my_turn:
        user1.my_turn = False
        user2.my_turn = True
    else:
        user1.my_turn = True
        user2.my_turn = False


        
