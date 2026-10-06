import os

from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from modules.admin import admin
from modules.pos import pos
from utils.get_available_options import get_available_options
from utils.int_input import int_input
from utils.terminal import write, clear_screen, move_cursor, from_bottom


def select_module():
    options = [
        MenuOption('POS', pos),
        MenuOption('Panel Administracyjny', admin)
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()
        move_cursor(1)
        write('System ERP')
        move_cursor(3)
        write('Wybierz odpowiedni moduł aplikacji:\n1. Wybierz liczbę z listy poniżej\n2. Naciśnij przycisk Enter')
        move_cursor(from_bottom(rows, len(options) + 1))
        write('Wybierz moduł:')

        bottom_nav_list(options, rows)

        if error_message:
            move_cursor(from_bottom(rows, len(options) + 3))
            write(error_message)

        move_cursor(rows)
        write(f'Wprwoadź liczbę: ({get_available_options(len(options))}) ')

        try:
            user_input = int_input(None)

            if user_input is None:
                raise TypeError

            if user_input <= 0:
                raise IndexError

            selected_option = options[user_input - 1]
        except (ValueError, TypeError):
            error_message = 'To nie jest liczba! Wprowadź opcje ponownie'
        except IndexError:
            error_message = f'Nie ma opcji nr {user_input}'
        else:
            selected_option.execute()
            break
