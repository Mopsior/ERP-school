import os

from classes.promotion_input_method import PromotionInputMethod
from utils.admin.add_promotion import add_promotion
from utils.admin.product_inputs import product_price_input
from utils.admin.promotion_inputs import promotion_name_input
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from classes.promotion import Promotion


def create_promotion():
    promotion_name: str | None = None
    promotion_percentage: float | None = None

    error_message: str | None = None

    promotion_input_method: PromotionInputMethod = PromotionInputMethod.NAME

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write("Dodaj nową promocję")

        if promotion_name:
            move_cursor(3)
            write("Nazwa:")
            move_cursor(4)
            write(promotion_name)

        if promotion_percentage is not None:
            move_cursor(6)
            write("Rabat:")
            move_cursor(7)
            write(f"{promotion_percentage} %")

        if error_message:
            move_cursor(from_bottom(rows, 4))
            write(error_message)

        move_cursor(from_bottom(rows, 1))
        match promotion_input_method:
            case PromotionInputMethod.NAME:
                write("Wprowadź nazwę promocji:")
            case PromotionInputMethod.PERCENTAGE:
                write("Wprowadź procent rabatu:")

        move_cursor(rows)

        try:
            match promotion_input_method:
                case PromotionInputMethod.NAME:
                    promotion_name = promotion_name_input()
                    promotion_input_method = PromotionInputMethod.PERCENTAGE
                    continue
                case PromotionInputMethod.PERCENTAGE:
                    product_price = product_price_input()
                    promotion_percentage = product_price

                    assert isinstance(promotion_name, str)
                    assert isinstance(promotion_percentage, float)

                    new_promotion = Promotion(
                        name=promotion_name,
                        percentage=promotion_percentage,
                        active=True
                    )

                    add_promotion(new_promotion)
        except (TypeError, ValueError) as e:
            error_message = str(e)
        else:
            error_message = None
            break