from classes.menu_option import MenuOption
from utils.terminal import move_cursor, from_bottom, write


def bottom_nav_list(options: list[MenuOption], rows: int):
    for i, option in enumerate(options):
        move_cursor(from_bottom(rows, len(options) - i))
        write(f'({i + 1}) {option.name}')