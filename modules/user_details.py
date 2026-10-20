import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from utils.get_available_options import get_available_options
from utils.get_users import get_users
from utils.int_input import int_input
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from utils.remove_user import remove_user


def user_details(user_id: int):
    from modules.admin import admin

    users = get_users()
    if not users: raise FileNotFoundError

    selected_user = users[user_id]

    clear_screen()
    move_cursor(1)
    write(f'Wybrano uzytkownikoa {selected_user['name']}')

    action_options = [
        MenuOption('Dodaj', lambda: user_details(user_id)),
        MenuOption('Edytuj', lambda: user_details(user_id)),
        MenuOption('Usuń', lambda: remove_user(user_id)),
        MenuOption('<- Powrót', lambda : admin(AdminInputMode.PAGE_CONTENT))
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write('Informacje o użytkowniku')
        move_cursor(3)
        write(f'ID:     {user_id}')
        move_cursor(4)
        write(f'Nazwa:  {selected_user['name']}')
        move_cursor(5)
        write(f'Rola:   {selected_user['role']}')

        move_cursor(from_bottom(rows, len(action_options) + 1))
        write('Wybierz akcję:')
        bottom_nav_list(action_options, rows)

        if error_message:
            move_cursor(from_bottom(rows, len(action_options) + 3))
            write(error_message)

        move_cursor(rows)
        write(f'Wprwoadź liczbę: ({get_available_options(len(action_options))}) ')

        user_input = None
        try:
            user_input = int_input(None)

            if user_input is None:
                raise TypeError

            if user_input <= 0:
                raise IndexError

            selected_option = action_options[user_input - 1]
        except (ValueError, TypeError):
            error_message = 'To nie jest liczba! Wprowadź opcje ponownie'
        except IndexError:
            error_message = f'Nie ma opcji nr {user_input}'
        else:
            selected_option.execute()
            break