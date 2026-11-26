import os

from classes.menu_option import MenuOption
from classes.promotion_input_method import PromotionInputMethod
from components.action_selection import action_selection
from utils.admin.edit_promotion import edit_promotion
from utils.admin.get_promotions import get_promotions
from utils.admin.promotion_inputs import promotion_name_input, promotion_percentage_input, promotion_active_input
from utils.chars import checkmark, crossmark
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from classes.promotion import Promotion


def update_promotion(promotion_id: int):
    promotions = get_promotions()
    promotion = promotions[promotion_id]

    promotion_name: str | None = None
    promotion_percentage: float | None = None
    promotion_active: bool | None = None

    error_message: str | None = None
    error_row: int = 4

    promotion_input_method: PromotionInputMethod = PromotionInputMethod.NAME

    confirmation_options = [
        MenuOption("Zapisz", data=True),
        MenuOption("Anuluj", data=False)
    ]

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write(f"Edytuj promocję")
        move_cursor(2)
        write("Kliknij Enter, aby zostawić poprzednie wartości")

        if promotion_name:
            move_cursor(4)
            write("Nazwa:")
            move_cursor(5)
            write(promotion_name)

        if promotion_percentage is not None:
            move_cursor(7)
            write("Zniżka (%):")
            move_cursor(8)
            write(f"{promotion_percentage}")

        if promotion_active is not None:
            move_cursor(10)
            write("Aktywna:")
            move_cursor(11)
            write(f"{checkmark if promotion_active else crossmark}")

        if error_message:
            move_cursor(from_bottom(rows, error_row))
            write(error_message)

        move_cursor(from_bottom(rows, 1))
        match promotion_input_method:
            case PromotionInputMethod.NAME:
                error_row = 4
                write("Wprowadź nazwę promocji")
                move_cursor(rows)
                write(f'({promotion["name"]}): ')
            case PromotionInputMethod.PERCENTAGE:
                error_row = 4
                write("Wprowadź zniżkę (%):")
                move_cursor(rows)
                write(f'({promotion["percentage"]:.2f}): ')
            case PromotionInputMethod.ACTIVE:
                error_row = 4
                write("Czy promocja jest aktywna? (tak/nie):")
                move_cursor(rows)
                write(f'({"tak" if promotion["active"] else "nie"}): ')
            case PromotionInputMethod.CONFIRMATION:
                error_row = len(confirmation_options) + 3

        try:
            match promotion_input_method:
                case PromotionInputMethod.NAME:
                    promotion_name = promotion_name_input(promotion['name'])
                    promotion_input_method = PromotionInputMethod.PERCENTAGE
                    continue
                case PromotionInputMethod.PERCENTAGE:
                    promotion_percentage = promotion_percentage_input(promotion['percentage'])
                    promotion_input_method = PromotionInputMethod.ACTIVE
                    continue
                case PromotionInputMethod.ACTIVE:
                    promotion_active = promotion_active_input(promotion['active'])
                    promotion_input_method = PromotionInputMethod.CONFIRMATION
                    continue
                case PromotionInputMethod.CONFIRMATION:
                    selected_option, error_message = action_selection(
                        confirmation_options, rows, 'Wybierz akcję:', error_message
                    )

                    if selected_option is None:
                        continue

                    match selected_option.data:
                        case True:
                            assert isinstance(promotion_name, str)
                            assert isinstance(promotion_percentage, float)
                            assert isinstance(promotion_active, bool)

                            new_promotion = Promotion(
                                name=promotion_name,
                                percentage=promotion_percentage,
                                active=promotion_active
                            )

                            edit_promotion(new_promotion, promotion_id)
                        case False:
                            from modules.admin.promotion_details import promotion_details

                            promotion_details(promotion_id)
        except (TypeError, ValueError) as e:
            error_message = str(e)
        else:
            error_message = None
            break