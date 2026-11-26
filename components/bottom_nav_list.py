from classes.menu_option import MenuOption
from utils.terminal import move_cursor, from_bottom, write


def bottom_nav_list(options: list[MenuOption], rows: int) -> int:
    visible_options = list(filter(lambda o: o.hidden_from_list is False, options))
    visible_length = len(visible_options)
    actual_row = visible_length
    with_return = any(option.is_return for option in options)

    for i, option in enumerate(options):
        if option.hidden_from_list: continue
        move_cursor(from_bottom(rows, actual_row))
        write(f'({i + 1 if not option.is_return else ":q"}) {" " if with_return and not option.is_return else ""}{option.name}')
        actual_row -= 1

    return visible_length