def find_figure_by_position(all_figures, position):
    for figure in all_figures:
        if figure.current_position == position:
            return figure
    


def checking_squares_for_bishops(bishop, board, up_number, down_number, up_letter, down_letter, all_squares):
    possible_move_uu = f'{up_letter} + {up_number}'
    figure_uu = find_figure_by_position(board.all_figures, possible_move_uu)
    possible_move_ud = f'{up_letter} + {down_number}'
    figure_ud = find_figure_by_position(board.all_figures, possible_move_ud)
    possible_move_du = f'{down_letter} + {up_number}'
    figure_du = find_figure_by_position(board.all_figures, possible_move_du)
    possible_move_dd = f'{down_letter} + {down_number}'
    figure_dd = find_figure_by_position(board.all_figures, possible_move_dd)

    if (possible_move_uu in all_squares) and (possible_move_uu not in board.taken_squares):
        bishop.possible_moves.append(possible_move_uu)

    if (possible_move_uu in all_squares) and (possible_move_uu in board.taken_squares) \
    and (leap_uu < 1) and (bishop.color != figure_uu.color):
        bishop.possible_moves.append(possible_move_uu)
        leap_uu +=1
        
        
