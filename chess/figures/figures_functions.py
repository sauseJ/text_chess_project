def find_figure_by_position(all_figures, position):
    for figure in all_figures:
        if figure.current_position == position:
            return figure
    


def checking_diogonals(figure, board, up_number, down_number, up_letter, down_letter, all_squares, leap_uu=0, leap_ud=0, leap_du=0, leap_dd=0):
    chr_up_letter = chr(up_letter)
    chr_down_letter = chr(down_letter)

    possible_move_uu = f'{chr_up_letter} + {up_number}'
    figure_uu = find_figure_by_position(board.all_figures, possible_move_uu)
    possible_move_ud = f'{chr_up_letter} + {down_number}'
    figure_ud = find_figure_by_position(board.all_figures, possible_move_ud)
    possible_move_du = f'{chr_down_letter} + {up_number}'
    figure_du = find_figure_by_position(board.all_figures, possible_move_du)
    possible_move_dd = f'{chr_down_letter} + {down_number}'
    figure_dd = find_figure_by_position(board.all_figures, possible_move_dd)

    if (possible_move_uu in all_squares) and (possible_move_uu not in board.taken_squares):
        figure.possible_moves.append(possible_move_uu)

    if (possible_move_uu in all_squares) and (possible_move_uu in board.taken_squares) \
    and (leap_uu < 1) and (figure.color != figure_uu.color):
        figure.possible_moves.append(possible_move_uu)
        leap_uu +=1
        
        
    if (possible_move_ud in all_squares) and (possible_move_ud not in board.taken_squares):
        figure.possible_moves.append(possible_move_ud)

    if (possible_move_ud in all_squares) and (possible_move_ud in board.taken_squares) \
    and (leap_ud < 1) and (figure.color != figure_ud.color):
        figure.possible_moves.append(possible_move_ud)
        leap_ud +=1

        
    if (possible_move_du in all_squares) and (possible_move_du not in board.taken_squares):
        figure.possible_moves.append(possible_move_du)

    if (possible_move_du in all_squares) and (possible_move_du in board.taken_squares) \
    and (leap_du < 1) and (figure.color != figure_du.color):
        figure.possible_moves.append(possible_move_du)
        leap_du +=1

        
    if (possible_move_dd in all_squares) and (possible_move_dd not in board.taken_squares):
        figure.possible_moves.append(possible_move_dd)

    if (possible_move_dd in all_squares) and (possible_move_dd in board.taken_squares) \
    and (leap_dd < 1) and (figure.color != figure_dd.color):
        figure.possible_moves.append(possible_move_dd)
        leap_dd +=1
        
def checking_all_sides(figure, board, letter, number, up_number, down_number, up_letter, down_letter, all_squares, leap_u=0, leap_d=0, leap_l=0, leap_r=0):
    chr_up_letter = chr(up_letter)
    chr_down_letter = chr(down_letter)
    chr_letter = chr(letter)

    possible_move_u = f'{chr_letter} + {up_number}'
    figure_u = find_figure_by_position(board.all_figures, possible_move_u)
    possible_move_d = f'{chr_letter} + {down_number}'
    figure_d = find_figure_by_position(board.all_figures, possible_move_d)
    possible_move_r = f'{chr_up_letter} + {number}'
    figure_l = find_figure_by_position(board.all_figures, possible_move_r)
    possible_move_l = f'{chr_down_letter} + {number}'
    figure_r = find_figure_by_position(board.all_figures, possible_move_l)

    if (possible_move_u in all_squares) and (possible_move_u not in board.taken_squares):
        figure.possible_moves.append(possible_move_u)

    if (possible_move_u in all_squares) and (possible_move_u in board.taken_squares) \
    and (leap_u < 1) and (figure.color != figure_u.color):
        figure.possible_moves.append(possible_move_u)
        leap_u +=1


    if (possible_move_d in all_squares) and (possible_move_d not in board.taken_squares):
        figure.possible_moves.append(possible_move_d)

    if (possible_move_d in all_squares) and (possible_move_d in board.taken_squares) \
    and (leap_d < 1) and (figure.color != figure_d.color):
        figure.possible_moves.append(possible_move_d)
        leap_d +=1

    
    if (possible_move_l in all_squares) and (possible_move_l not in board.taken_squares):
        figure.possible_moves.append(possible_move_l)

    if (possible_move_l in all_squares) and (possible_move_l in board.taken_squares) \
    and (leap_l < 1) and (figure.color != figure_l.color):
        figure.possible_moves.append(possible_move_l)
        leap_l +=1


    if (possible_move_r in all_squares) and (possible_move_u not in board.taken_squares):
        figure.possible_moves.append(possible_move_u)

    if (possible_move_r in all_squares) and (possible_move_r in board.taken_squares) \
    and (leap_r < 1) and (figure.color != figure_r.color):
        figure.possible_moves.append(possible_move_r)
        leap_r +=1


def checking_squares_for_knight(figure, board, number, letter, xnumber, xletter, all_squares):
    chr_xletter = chr(xletter)
    chr_letter = chr(letter)

    for y in range(-1, 2, 1):
        if y == 0: continue
        yletter = chr_letter + y
        chr_yletter = chr(yletter)
        ynumber = number + y

        possible_move_num = f'{chr_yletter} + {xnumber}'
        possible_move_let = f'{chr_xletter} + {ynumber}'

        if possible_move_num in all_squares:
            if possible_move_num not in board.taken_squares:
                figure.possible_moves.append(possible_move_num)
            else:
                if find_figure_by_position(board.all_figures, possible_move_num).color != figure.color:
                    figure.possible_moves.append(possible_move_num)
        
        if possible_move_let in all_squares:
            if possible_move_let not in board.taken_squares:
                figure.possible_moves.append(possible_move_let)
            else:
                if find_figure_by_position(board.all_figures, possible_move_let).color != figure.color:
                    figure.possible_moves.append(possible_move_let)

def checking_protection(figure, board):
    figure.is_protected = False
    
    for f in board.all_figures:
        if (figure.current_position in f.possible_moves) and (figure.color == f.color):
            figure.is_protected = True
        