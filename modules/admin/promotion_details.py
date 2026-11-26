import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from modules.admin.promotions import promotions_list
from utils.admin.get_promotions import get_promotions
from utils.admin.remove_promotion import remove_promotion
from utils.chars import checkmark, crossmark
from utils.terminal import clear_screen, move_cursor, write


def promotion_details(promotion_id: int):
    from modules.admin.update_promotion import update_promotion

    promotions = get_promotions()
    selected_promotion = promotions[promotion_id]

    action_options = [
        MenuOption('Edytuj', lambda: update_promotion(promotion_id)),
        MenuOption('Usuń', lambda: remove_promotion(promotion_id)),
        MenuOption('<- Powrót', lambda : promotions_list(AdminInputMode.PAGE_CONTENT))
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write('Informacje o promocji')
        move_cursor(3)
        write(f'ID:      {promotion_id + 1}')
        move_cursor(4)
        write(f'Nazwa:   {selected_promotion['name']}')
        move_cursor(5)
        write(f'Rabat:   {selected_promotion['percentage']} %')
        move_cursor(6)
        write(f'Aktywna: {checkmark if selected_promotion['active'] else crossmark}')

        selected_option, error_message = action_selection(
            action_options, rows, 'Wybierz akcję:', error_message
        )

        if selected_option:
            selected_option.execute()
            break