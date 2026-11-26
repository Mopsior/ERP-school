import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from components.empty import empty
from components.promotions_table import promotions_table
from components.tabs import tabs
from utils.admin.get_promotions import get_promotions
from utils.terminal import clear_screen


def promotions_list(input_mode: AdminInputMode | None = AdminInputMode.SELECTING):
    from modules.admin.admin import admin
    from modules.admin.products import products_list

    promotions = get_promotions()

    input_mode_options = [
        MenuOption('Zakładkę', lambda: promotions_list(AdminInputMode.TABS)),
        MenuOption('Promocje', lambda: promotions_list(AdminInputMode.PAGE_CONTENT))
    ]

    tab_options = [
        MenuOption('Użytkownicy', admin),
        MenuOption('Produkty', products_list),
        MenuOption('Promocje', promotions_list, selected=True),
        MenuOption('<- Wróć', promotions_list, hidden_from_tabs=True)
    ]

    page_options: list[MenuOption] = []

    if promotions:
        for i, product in enumerate(promotions):
            page_options.append(MenuOption(product['name'], lambda i=i:None))

    page_options.append(MenuOption('+ Dodaj promocję', None))
    page_options.append(MenuOption('<- Wróć', products_list))

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        tabs(tab_options)

        if promotions:
            promotions_table(promotions, 3)
        else:
            empty(3, "Nie ma jeszcze żadnej promocji. Stwórz pierwszą z opcji poniżej")

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