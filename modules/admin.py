import os

from classes.menu_option import MenuOption
from components.tabs import tabs
from components.user_table import user_table
from utils.get_users import get_users
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

    users = get_users()
    if not users: raise FileNotFoundError

    user_table(users, 5)

    move_cursor(columns)
    input()
