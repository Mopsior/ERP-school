import os

from classes.menu_option import MenuOption
from classes.pos_input_mode import POSInputMode
from components.bottom_nav_list import bottom_nav_list
from components.empty import empty
from components.products_table import products_table
from components.tabs import tabs
from utils.admin.get_products import get_products
from utils.get_available_options import get_available_options
from utils.int_input import int_input
from utils.terminal import clear_screen, move_cursor, from_bottom, write


def pos_products(input_mode: POSInputMode | None = POSInputMode.SELECTING):
    products = get_products()

    input_mode_options = [
        MenuOption('Zakładkę', lambda: pos_products(POSInputMode.TABS)),
        MenuOption('Produkt', lambda: pos_products(POSInputMode.PAGE_CONTENT))
    ]

    tab_options = [
        MenuOption('Produkty', pos_products, selected=True),
        MenuOption('Promocje', pos_products),
        MenuOption('Kody rabatowe', pos_products),
        MenuOption('<- Wróć', pos_products, hidden_from_tabs=True)
    ]

    page_options: list[MenuOption] = []

    if products:
        for i, product in enumerate(products):
            page_options.append(MenuOption(product['name'], pos_products))

    page_options.append(MenuOption('<- Wróć', pos_products))

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        tabs(tab_options)

        if products:
            products_table(products, 3)
        else:
            empty(3, "Nie ma jeszcze żadnego produktu. Skontaktuj się z właścicielem sklepu, aby dodał nowe")

        size_source = {
            POSInputMode.SELECTING: input_mode_options,
            POSInputMode.TABS: tab_options,
            POSInputMode.PAGE_CONTENT: page_options
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
            user_input = int_input()

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