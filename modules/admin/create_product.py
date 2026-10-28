import os

from classes.product_input_method import ProductInptuMethod
from utils.admin.add_product import add_product
from utils.admin.product_inputs import product_name_input, product_price_input
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from classes.product import Product

def create_product():
    product_name: str | None = None
    product_price: float | None = None

    error_message: str | None = None

    product_input_method: ProductInptuMethod = ProductInptuMethod.NAME

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write("Dodaj nowy produkt")

        if product_name:
            move_cursor(3)
            write("Nazwa:")
            move_cursor(4)
            write(product_name)

        if error_message:
            move_cursor(from_bottom(rows, 4))
            write(error_message)

        move_cursor(from_bottom(rows, 1))
        match product_input_method:
            case ProductInptuMethod.NAME:
                write("Wprowadź nazwę produktu:")
            case ProductInptuMethod.PRICE:
                write("Wprowadź cenę:")

        move_cursor(rows)

        try:
            match product_input_method:
                case ProductInptuMethod.NAME:
                    product_name = product_name_input()
                    product_input_method = ProductInptuMethod.PRICE
                    continue
                case ProductInptuMethod.PRICE:
                    product_price = product_price_input()

                    assert isinstance(product_name, str)
                    assert isinstance(product_price, float)

                    new_product = Product(
                        name=product_name,
                        price=product_price
                    )

                    add_product(new_product)
        except (TypeError, ValueError) as e:
            error_message = str(e)
        else:
            error_message = None
            break