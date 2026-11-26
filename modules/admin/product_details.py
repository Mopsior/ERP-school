import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from utils.admin.get_products import get_products
from utils.admin.remove_product import remove_product
from utils.terminal import clear_screen, move_cursor, write


def product_details(product_id: int):
    from modules.admin.products import products_list
    from modules.admin.update_product import update_product

    products = get_products()

    selected_product = products[product_id]

    action_options = [
        MenuOption('Edytuj', lambda: update_product(product_id)),
        MenuOption('Usuń', lambda: remove_product(product_id)),
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
        write(f'Cena:   {selected_product['price']:.2f}')

        selected_option, error_message = action_selection(
            action_options, rows, 'Wybierz akcję:', error_message
        )

        if selected_option:
            selected_option.execute()
            break