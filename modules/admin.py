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
