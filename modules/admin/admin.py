import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from components.tabs import tabs
from components.user_table import user_table
from modules.admin.create_user import create_user
from modules.admin.products import products_list
from modules.admin.promotions import promotions_list
from modules.admin.user_details import user_details
from utils.admin.get_users import get_users
from utils.terminal import clear_screen

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
        MenuOption('Promocje', promotions_list),
        MenuOption('<- Wróć', admin, hidden_from_tabs=True, is_return=True)
    ]

    page_options: list[MenuOption] = []

    for i, user in enumerate(users):
        page_options.append(MenuOption(user['name'], lambda i=i: user_details(i)))

    page_options.append(MenuOption('+ Dodaj użytkownika', create_user))
    page_options.append(MenuOption('<- Wróć', admin, is_return=True))

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

        selected_option, error_message = action_selection(
            size_source, rows, 'Wybierz:', error_message
        )

        if selected_option:
            selected_option.execute()