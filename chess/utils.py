import random
from chess.figures import figures_functions as ff
from chess.figures import Pawn, Bishop, King, Knight, Queen, Rook

def find_figure_by_possible_move(all_figures, move, type, user):
    possible_figures = []
    for figure in all_figures:
        if (isinstance(figure, type)) and (move[-2:] in figure.possible_moves) and (figure.color == user.color):
            possible_figures.append(figure)
    
    if len(possible_figures) > 1:
        for figure in possible_figures:
            if type == Pawn.Pawn:
                if figure.current_position[0] == move[0]:
                    return figure
            else:
                if figure.current_position[0] == move[1]:
                    return figure
    else:
        return possible_figures[0]


def find_my_king(user, board):
    for king in board.all_figures:
        if (king.color == user.color) and (isinstance(king, King.King)):
            return king

def pawn_promotion(pawn, board, move):
    if ((pawn.color == 'w') and (move[-3] == '8')) or((pawn.color == 'b') and (move[-3] == '1')):
        if move[-1] == 'Q':
            queen = Queen.Queen(board, 'Q' + move[-4:-2], pawn.color, move[-4:-2], is_protected = False)
            ff.checking_protection(queen, board)
            pawn.is_alive = False
            return queen
        elif move[-1] == 'R':
            rook = Rook.Rook(board, 'R' + move[-4:-2], pawn.color, move[-4:-2], is_protected = False)
            ff.checking_protection(rook, board)
            pawn.is_alive = False
            return rook
        elif move[-1] == 'B':
            bishop = Bishop.Bishop(board, 'B' + move[-4:-2], pawn.color, move[-4:-2], is_protected = False)
            ff.checking_protection(bishop, board)
            pawn.is_alive = False
            return bishop
        elif move[-1] == 'N':
            knight = Knight.Knight(board, 'N' + move[-4:-2], pawn.color, move[-4:-2], is_protected = False)
            ff.checking_protection(knight, board)
            pawn.is_alive = False
            return knight
        else: print('Impossible promotion')



def register_user(user):
    user.name = input('Stage your name: ')
    user.age = input('Stage your age too: ')
    user.sexual_orientation = input('Are you gay or something? ')
    print('Enjoy terminal chess!')

def change_colors(user1, user2):
    color = user1.color
    user1.color = user2.color
    user2.color = color
    return user1, user2

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
    return user1, user2
def figure_check(move, board, user):
    letter = move[0]
    if letter == 'B':
        bishop = find_figure_by_possible_move(board.all_figures, move, Bishop.Bishop, user)
        return bishop
    elif letter == 'N':
        knight = find_figure_by_possible_move(board.all_figures, move, Knight.Knight, user)
        return knight
    elif letter == 'R':
        rook = find_figure_by_possible_move(board.all_figures, move, Rook.Rook, user)
        return rook
    elif letter == 'Q':
        queen = find_figure_by_possible_move(board.all_figures, move, Queen.Queen, user)
        return queen
    elif letter == 'K':
        king = find_figure_by_possible_move(board.all_figures, move, King.King, user)
        return king
    elif letter in ['a','b','c','d','e','f','g','h']:
        pawn = find_figure_by_possible_move(board.all_figures, move, Pawn.Pawn, user)
        #if '=' in move:
        #   new_figure = ff.pawn_promotion(pawn, board, move)
        #   return new_figure
        #else:
        return pawn
        


def action(user, board):
    
    try:
        move = input(f'{user.name}, what\'s your move then: ')
        if move == 'O-O' or move == '0-0':
            find_my_king(user, board).short_castle(board)
        elif move == 'O-O-O' or move == '0-0-0':
            find_my_king(user, board).long_castle(board)
        else:
            figure = figure_check(move, board, user)
            prev_pos = figure.current_position
            
            if 'x' in move:
                opponent_figure = ff.find_figure_by_position(board.all_figures, move[-2:])
                figure.take(move[-2:], opponent_figure)
            else:
                figure.move(move[-2:])
        
        check_checking(user, board, figure, prev_pos)

        return move, board.all_figures

    except IndexError:
        print('Nah man, come on! Try again')
        return action(user, board)


        


        

def check_for_mate(user, board):
    my_king = find_my_king(user, board)

    if (moves_checking(user, board)) and (my_king.in_check == True):
        return True
    else:
        return False

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

def check_for_stalemate(user, board):
    my_king = find_my_king(user, board)

    if (moves_checking(user, board)) and (my_king.in_check == False):
        return True
    else:
        return False

                
def checking_king_v_king_draw(board):
    return (len(board.all_figures) == 2)

def checking_last_fifty_moves(moves):
    count = 0

    if len(moves) < 50:
        return False
    else:
        for i in range(1, 51):
            for m in range(2):
                key = list(moves)[-i]
                values = moves[key]
                
                if ('x' in values[m]) or (values[m][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
                    count +=1
        
        return count == 0

def check_repetition(positions_list):  
    for position in positions_list:
        #sorted_position = position.sort()
        #n = positions_list.count(sorted_position)
        n = positions_list.count(position)
        return n == 3
    
    return False

def checking_king_bishop_vs_king(board):
    if len(board.all_figures) == 3:
        for figure in board.all_figures:
            if isinstance(figure, Bishop.Bishop):
                return True
        return False

    return False

def checking_king_knight_vs_king(board):
    if len(board.all_figures) == 3:
        for figure in board.all_figures:
            if isinstance(figure, Knight.Knight):
                return True
        return False
    
    return False

def checking_king_bishop_vs_king_bishop(board):
    bishops = []

    if len(board.all_figures) == 4:
        for figure in board.all_figures:
            if isinstance(figure, Bishop.Bishop):
                bishops.append(figure)
    
        if (len(bishops) == 2) and (bishops[0].bcolor is bishops[1].bcolor):
            return True
        
        return False
    return False

def checking_for_draws(user, board, positions_list, moves):
    a = check_for_stalemate(user, board)
    #b = check_repetition(positions_list)
    c = checking_king_v_king_draw(board)
    d = checking_king_bishop_vs_king(board)
    e = checking_king_knight_vs_king(board)
    f = checking_last_fifty_moves(moves)
    g = checking_king_bishop_vs_king_bishop(board)

    if a or c or d or e or f or g:
        return True
    return False

def check_checking(user, board, figure, prev_pos):
    af = board.all_figures.copy()
    ts = board.taken_squares.copy()
    
    
    board.refresh()
    king = find_my_king(user, board)
    king.am_i_in_check(board)

    if king.in_check == True:
        board.all_figures = af
        board.taken_squares = ts
        figure.current_position = prev_pos
        raise IndexError("You're still in check")
    else:
        return

def moves_checking(user, board):
    king = find_my_king(user, board)
    king.am_i_in_check(board)
    if king.in_check == False:
        return False
    

    pm = 0
    enemy = None

    for figure in board.all_figures:
        if figure.color == user.color:
            af = board.all_figures.copy()
            ts = board.taken_squares.copy()
            
            if figure.possible_moves:
                for move in figure.possible_moves:
                    if move in board.taken_squares:
                        enemy = ff.find_figure_by_position(board.all_figures, move)
                        enemy.is_alive = False
                    
                    prev_pos = figure.current_position
                    figure.current_position = move
                    board.refresh()
                    king = find_my_king(user, board)
                    king.am_i_in_check(board)

                    if king.in_check == True:
                        board.all_figures = af
                        board.taken_squares = ts
                        figure.current_position = prev_pos
                        if enemy:
                            enemy.is_alive = True
                            enemy.current_position = move
                    else:
                        board.all_figures = af
                        board.taken_squares = ts
                        figure.current_position = prev_pos
                        if enemy:
                            enemy.is_alive = True
                            enemy.current_position = move 
                        pm += 1
                    
                    board.refresh()

    return pm == 0



            
