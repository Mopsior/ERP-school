import os

from classes.menu_option import MenuOption
from classes.user_data_input_method import UserDataInputMethod
from classes.user_role import UserRole
from components.bottom_nav_list import bottom_nav_list
from utils.admin.edit_user import edit_user
from utils.get_available_options import get_available_options
from utils.admin.get_role_index import get_role_index
from utils.admin.get_users import get_users
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from utils.admin.user_data_inputs import user_name_input, user_role_input, user_confirmation_input
from classes.user import User


def update_user(user_id: int):
    from modules.admin.user_details import user_details

    users = get_users()
    if not users: raise FileNotFoundError
    if user_id > len(users): raise IndexError
    user = users[user_id]

    user_name: str | None = None
    user_role: UserRole | None = None
    user_confirmation: bool | None = None

    error_message: str | None = None
    error_row: int = 0

    user_data_input_method: UserDataInputMethod = UserDataInputMethod.NAME

    user_roles_list = [
        MenuOption("Pracownik", data=UserRole.WORKER),
        MenuOption("Admin", data=UserRole.ADMIN)
    ]

    confirmation_options = [
        MenuOption("Zapisz", data=True),
        MenuOption("Anuluj", data=False)
    ]

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write("Edytuj użytkownika")
        move_cursor(3)
        write("Kliknij Enter, aby zostawić poprzednie wartości")

        if user_name:
            move_cursor(5)
            write('Nazwa:')
            move_cursor(6)
            write(user_name)

        if user_role:
            move_cursor(8)
            write('Rola:')
            move_cursor(9)
            write(str(user_role))

        if error_message:
            move_cursor(from_bottom(rows, error_row))
            write(error_message)

        match user_data_input_method:
            case UserDataInputMethod.NAME:
                error_row = 3
                move_cursor(from_bottom(rows, 1))
                write("Wprowadź nazwę użytkownika:")
                move_cursor(rows)
                write(f"({user['name']}): ")
            case UserDataInputMethod.ROLE:
                error_row = len(user_roles_list) + 3
                move_cursor(from_bottom(rows, len(user_roles_list) + 1))
                write("Wprowadź rolę użytkownika:")
                bottom_nav_list(user_roles_list, rows)
                move_cursor(rows)
                selected_role = get_role_index(user_roles_list, user['role'])
                write(f'Wprwoadź liczbę: ({get_available_options(len(user_roles_list), selected_role)}) ')
            case UserDataInputMethod.CONFIRMATION:
                error_row = len(confirmation_options) + 3
                move_cursor(from_bottom(rows, len(confirmation_options) + 1))
                write("Czy chcesz zapisać zmiany?")
                bottom_nav_list(confirmation_options, rows)
                move_cursor(rows)
                write(f'Wprwoadź liczbę: ({get_available_options(len(confirmation_options))}) ')

        try:
            match user_data_input_method:
                case UserDataInputMethod.NAME:
                    user_name = user_name_input(user['name'])
                    user_data_input_method = UserDataInputMethod.ROLE
                    continue
                case UserDataInputMethod.ROLE:
                    user_role = user_role_input(user_roles_list, user['role'])
                    user_data_input_method = UserDataInputMethod.CONFIRMATION
                    continue
                case UserDataInputMethod.CONFIRMATION:
                    user_confirmation = user_confirmation_input(confirmation_options)
                    match user_confirmation:
                        case True:
                            assert isinstance(user_name, str)
                            assert isinstance(user_role, UserRole)

                            new_user = User(
                                name=user_name,
                                role=user_role,
                                password=user['password']
                            )

                            edit_user(new_user, user_id)
                        case False:
                            user_details(user_id)
                    break
        except TypeError as e:
            error_message = str(e)
        else:
            error_message = None
            break