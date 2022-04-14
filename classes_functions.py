def find_figure_by_position(all_figures, position):
    for figure in all_figures:
        if figure.current_position == position:
            return figure

