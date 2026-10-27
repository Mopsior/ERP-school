import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from components.tabs import tabs
from components.user_table import user_table
from modules.admin.create_user import create_user
from modules.admin.products import products_list
from modules.admin.user_details import user_details
from utils.get_available_options import get_available_options
from utils.admin.get_users import get_users
from utils.int_input import int_input
from utils.terminal import clear_screen, move_cursor, write, from_bottom

def admin(input_mode: AdminInputMode | None = AdminInputMode.SELECTING):
    users = get_users()
    if not users: raise FileNotFoundError

    input_mode_options = [
        MenuOption('Zakładkę', lambda: admin(AdminInputMode.TABS)),
        MenuOption('Użytkownika', lambda: admin(AdminInputMode.PAGE_CONTENT))
    ]

    tab_options = [
        MenuOption('Użytkownicy', admin, selected=True),
        MenuOption('Produkty', products_list),
        MenuOption('<- Wróć', admin, hidden_from_tabs=True)
    ]

    page_options: list[MenuOption] = []

    for i, user in enumerate(users):
        page_options.append(MenuOption(user['name'], lambda i=i: user_details(i)))

    page_options.append(MenuOption('+ Dodaj użytkownika', create_user))
    page_options.append(MenuOption('<- Wróć', admin))

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        tabs(tab_options)

        user_table(users, 3)

        size_source = {
            AdminInputMode.SELECTING: input_mode_options,
            AdminInputMode.TABS: tab_options,
            AdminInputMode.PAGE_CONTENT: page_options
        }.get(input_mode)

        move_cursor(from_bottom(rows, len(size_source) + 1))
        write('Wybierz:')
        bottom_nav_list(size_source, rows)

        if error_message:
            move_cursor(from_bottom(rows, len(size_source) + 3))
            write(error_message)

        move_cursor(rows)
        write(f'Wprwoadź liczbę: ({get_available_options(len(size_source))}) ')

        user_input = None
        try:
            user_input = int_input(None)

            if user_input is None:
                raise TypeError

            if user_input <= 0:
                raise IndexError

            selected_option = size_source[user_input - 1]
        except (ValueError, TypeError):
            error_message = 'To nie jest liczba! Wprowadź opcje ponownie'
        except IndexError:
            error_message = f'Nie ma opcji nr {user_input}'
        else:
            selected_option.execute()
            break