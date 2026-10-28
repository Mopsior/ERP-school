import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from components.empty import empty
from components.products_table import products_table
from components.tabs import tabs
from modules.admin.product_details import product_details
from utils.admin.get_products import get_products
from utils.chars import invert_text
from utils.get_available_options import get_available_options
from utils.int_input import int_input
from utils.terminal import clear_screen, move_cursor, from_bottom, write


def products_list(input_mode: AdminInputMode | None = AdminInputMode.SELECTING):
    from modules.admin.admin import admin

    products = get_products()

    input_mode_options = [
        MenuOption('Zakładkę', lambda: products_list(AdminInputMode.TABS)),
        MenuOption('Produkt', lambda: products_list(AdminInputMode.PAGE_CONTENT))
    ]

    tab_options = [
        MenuOption('Użytkownicy', admin),
        MenuOption('Produkty', products_list, selected=True),
        MenuOption('<- Wróć', products_list, hidden_from_tabs=True)
    ]

    page_options: list[MenuOption] = []

    if products:
        for i, product in enumerate(products):
            page_options.append(MenuOption(product['name'], lambda i=i: product_details(i)))

    page_options.append(MenuOption('+ Dodaj produkt', products_list))
    page_options.append(MenuOption('<- Wróć', products_list))

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        tabs(tab_options)

        if products:
            products_table(products, 3)
        else:
            empty(3, "Nie ma jeszcze żadnego produktu. Stwórz nowy z opcji poniżej")

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