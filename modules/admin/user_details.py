import os

from classes.input_mode import AdminInputMode
from classes.menu_option import MenuOption
from components.action_selection import action_selection
from modules.admin.update_user import update_user
from utils.admin.get_users import get_users
from utils.terminal import clear_screen, move_cursor, write
from utils.admin.remove_user import remove_user


def user_details(user_id: int):
    from modules.admin.admin import admin

    users = get_users()
    if not users: raise FileNotFoundError

    selected_user = users[user_id]

    action_options = [
        MenuOption('Edytuj', lambda: update_user(user_id)),
        MenuOption('Usuń', lambda: remove_user(user_id)),
        MenuOption('<- Powrót', lambda : admin(AdminInputMode.PAGE_CONTENT))
    ]

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write('Informacje o użytkowniku')
        move_cursor(3)
        write(f'ID:     {user_id + 1}')
        move_cursor(4)
        write(f'Nazwa:  {selected_user['name']}')
        move_cursor(5)
        write(f'Rola:   {selected_user['role']}')

        selected_option, error_message = action_selection(
            action_options, rows, 'Wybierz akcję:', error_message
        )

        if selected_option:
            selected_option.execute()
            break