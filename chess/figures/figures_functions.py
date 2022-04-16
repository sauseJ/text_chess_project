def find_figure_by_position(all_figures, position):
    for figure in all_figures:
        if figure.current_position == position:
            return figure
    


def checking_diogonals(figure, board, up_number, down_number, up_letter, down_letter, all_squares, leap_uu=0, leap_ud=0, leap_du=0, leap_dd=0):
#    figure.possible_moves = []

    possible_move_uu = f'{up_letter} + {up_number}'
    figure_uu = find_figure_by_position(board.all_figures, possible_move_uu)
    possible_move_ud = f'{up_letter} + {down_number}'
    figure_ud = find_figure_by_position(board.all_figures, possible_move_ud)
    possible_move_du = f'{down_letter} + {up_number}'
    figure_du = find_figure_by_position(board.all_figures, possible_move_du)
    possible_move_dd = f'{down_letter} + {down_number}'
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
        
