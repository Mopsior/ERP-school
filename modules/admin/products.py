import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from components.empty import empty
from components.products_table import products_table
from components.tabs import tabs
from modules.admin.create_product import create_product
from modules.admin.product_details import product_details
from utils.admin.get_products import get_products
from utils.terminal import clear_screen


def products_list(input_mode: AdminInputMode | None = AdminInputMode.SELECTING):
    from modules.admin.admin import admin
    from modules.admin.promotions import promotions_list

    products = get_products()

    input_mode_options = [
        MenuOption('Zakładkę', lambda: products_list(AdminInputMode.TABS)),
        MenuOption('Produkt', lambda: products_list(AdminInputMode.PAGE_CONTENT))
    ]

    tab_options = [
        MenuOption('Użytkownicy', admin),
        MenuOption('Produkty', products_list, selected=True),
        MenuOption('Promocje', promotions_list),
        MenuOption('<- Wróć', products_list, hidden_from_tabs=True, is_return=True)
    ]

    page_options: list[MenuOption] = []

    if products:
        for i, product in enumerate(products):
            page_options.append(MenuOption(product['name'], lambda i=i: product_details(i)))

    page_options.append(MenuOption('+ Dodaj produkt', create_product))
    page_options.append(MenuOption('<- Wróć', products_list, is_return=True))

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

        selected_option, error_message = action_selection(
            size_source, rows, 'Wybierz:', error_message
        )

        if selected_option:
            selected_option.execute()
            break