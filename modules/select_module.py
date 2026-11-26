import os

from classes.login_mode import LoginMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from modules.admin.admin import admin
from modules.login import login
from modules.pos.products import pos_products
from utils.terminal import write, clear_screen, move_cursor


def select_module():
    options = [
        MenuOption('POS', lambda: login(LoginMode.WORKER, pos_products)),
        MenuOption('Panel Administracyjny', lambda: login(LoginMode.ADMIN, admin))
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()
        move_cursor(1)
        write('System ERP')
        move_cursor(3)
        write('Wybierz odpowiedni moduł aplikacji:\n1. Wybierz liczbę z listy poniżej\n2. Naciśnij przycisk Enter')
        selected_option, error_message = action_selection(
            options, rows, 'Wybierz moduł:', error_message
        )

        if selected_option:
            selected_option.execute()
            break
