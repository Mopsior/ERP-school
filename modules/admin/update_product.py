import os

from classes.menu_option import MenuOption
from classes.product import Product
from classes.product_input_method import ProductInptuMethod
from components.bottom_nav_list import bottom_nav_list
from utils.admin.edit_product import edit_product
from utils.admin.get_products import get_products
from utils.admin.product_inputs import product_name_input, product_price_input, product_confirmation_input
from utils.get_available_options import get_available_options
from utils.terminal import clear_screen, move_cursor, write, from_bottom


def update_product(product_id: int):
    products = get_products()
    product = products[product_id]

    product_name: str | None = None
    product_price: float | None = None

    error_message: str | None = None
    error_row: int = 4

    product_input_method: ProductInptuMethod = ProductInptuMethod.NAME

    confirmation_options = [
        MenuOption("Zapisz", data=True),
        MenuOption("Anuluj", data=False)
    ]

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write(f"Edytuj produkt")
        move_cursor(2)
        write("Kliknij Enter, aby zostawić poprzednie wartości")

        if product_name:
            move_cursor(4)
            write("Nazwa:")
            move_cursor(5)
            write(product_name)

        if product_price is not None:
            move_cursor(7)
            write("Cena:")
            move_cursor(8)
            write(f"{product_price:.2f}")

        if error_message:
            move_cursor(from_bottom(rows, error_row))
            write(error_message)

        move_cursor(from_bottom(rows, 1))
        match product_input_method:
            case ProductInptuMethod.NAME:
                error_row = 4
                write("Wprowadź nazwę produktu")
                move_cursor(rows)
                write(f'({product['name']}): ')
            case ProductInptuMethod.PRICE:
                error_row = 4
                write("Wprowadź cenę:")
                move_cursor(rows)
                write(f'({product["price"]:.2f}): ')
            case ProductInptuMethod.CONFIRMATION:
                error_row = len(confirmation_options) + 3
                move_cursor(from_bottom(rows, len(confirmation_options) + 1))
                write("Czy chcesz zapisać zmiany?")
                bottom_nav_list(confirmation_options, rows)
                move_cursor(rows)
                write(f'Wprwoadź liczbę: ({get_available_options(len(confirmation_options))}) ')

        try:
            match product_input_method:
                case ProductInptuMethod.NAME:
                    product_name = product_name_input(product['name'])
                    product_input_method = ProductInptuMethod.PRICE
                    continue
                case ProductInptuMethod.PRICE:
                    product_price = product_price_input(product['price'])
                    product_input_method = ProductInptuMethod.CONFIRMATION
                    continue
                case ProductInptuMethod.CONFIRMATION:
                    user_confirmation = product_confirmation_input(confirmation_options)
                    match user_confirmation:
                        case True:
                            assert isinstance(product_name, str)
                            assert isinstance(product_price, float)

                            new_product = Product(
                                name=product_name,
                                price=product_price
                            )

                            edit_product(new_product, product_id)
        except (TypeError, ValueError) as e:
            error_message = str(e)
        else:
            error_message = None
            break