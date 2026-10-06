import os

from classes import menu_option
from classes.menu_option import MenuOption
from components.tabs import tabs
from utils.chars import invert_text, vertical_line, horizontal_line, top_connector, bottom_right, bottom_left
from utils.terminal import clear_screen, move_cursor, write


def admin():
    clear_screen()
    columns, rows = os.get_terminal_size()

    tab_options = [
        MenuOption('Użytkownicy', admin),
        MenuOption('Druga zakładka', admin)
    ]

    tabs(tab_options)
    move_cursor(3)

    # move_cursor(1)
    # write(' ')
    # write(invert_text('UŻYTKOWNICY'))
    # write(f' {vertical_line} ')
    # write('Druga zakładka')
    # write(f' {vertical_line} ')
    # move_cursor(2)
    # write(horizontal_line*13 + top_connector + horizontal_line*16 + bottom_right)
    # move_cursor(3)