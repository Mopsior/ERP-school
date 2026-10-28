import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from utils.admin.get_products import get_products
from utils.get_available_options import get_available_options
from utils.int_input import int_input
from utils.terminal import clear_screen, move_cursor, write, from_bottom


def product_details(product_id: int):
    from modules.admin.products import products_list

    products = get_products()

    selected_product = products[product_id]

    action_options = [
        MenuOption('Edytuj', lambda: product_details(product_id)),
        MenuOption('Usuń', lambda: product_details(product_id)),
        MenuOption('<- Powrót', lambda : products_list(AdminInputMode.PAGE_CONTENT))
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write('Informacje o produkcie')
        move_cursor(3)
        write(f'ID:     {product_id + 1}')
        move_cursor(4)
        write(f'Nazwa:  {selected_product['name']}')
        move_cursor(5)
        write(f'Cena:   {selected_product['price']}')

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