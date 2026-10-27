import os

from classes.menu_option import MenuOption
from classes.user import User
from classes.user_data_input_method import UserDataInputMethod
from classes.user_role import UserRole
from components.bottom_nav_list import bottom_nav_list
from utils.add_user import add_user
from utils.get_available_options import get_available_options
from utils.terminal import clear_screen, move_cursor, write, from_bottom
from utils.user_data_inputs import user_name_input, user_role_input, user_password_input


def create_user():
    user_name: str | None = None
    user_role: UserRole | None = None
    user_password: str | None = None

    error_message: str | None = None
    error_row: int = 0

    user_data_input_method: UserDataInputMethod = UserDataInputMethod.NAME

    user_roles_list = [
        MenuOption("Pracownik", data=UserRole.WORKER),
        MenuOption("Admin", data=UserRole.ADMIN)
    ]

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write("Dodaj nowego użytkownika")

        if user_name:
            move_cursor(3)
            write('Nazwa:')
            move_cursor(4)
            write(user_name)

        if user_role:
            move_cursor(6)
            write('Rola:')
            move_cursor(7)
            write(str(user_role))

        if error_message:
            move_cursor(from_bottom(rows, error_row))
            write(error_message)

        input_method = user_name_input

        if user_data_input_method is UserDataInputMethod.NAME:
            error_row = 3
            move_cursor(from_bottom(rows, 1))
            write("Wprowadź nazwę użytkownika:")
            input_method = user_name_input
            move_cursor(rows)
        elif user_data_input_method is UserDataInputMethod.ROLE:
            error_row = len(user_roles_list) + 3
            move_cursor(from_bottom(rows, len(user_roles_list) + 1))
            write("Wprowadź rolę użytkownika:")
            bottom_nav_list(user_roles_list, rows)
            input_method = lambda: user_role_input(user_roles_list)
            move_cursor(rows)
            write(f'Wprwoadź liczbę: ({get_available_options(len(user_roles_list))}) ')

        elif user_data_input_method is UserDataInputMethod.PASSWORD:
            error_row = 3
            move_cursor(from_bottom(rows, 1))
            write("Wprowadź hasło użytkownika")
            input_method = user_password_input
            move_cursor(rows)

        try:
            user_input: str | UserRole | None = input_method()
        except TypeError as e:
            error_message = str(e)
        else:
            if user_data_input_method is UserDataInputMethod.NAME:
                error_message = None
                assert isinstance(user_input, str)
                user_name = user_input
                user_data_input_method = UserDataInputMethod.ROLE
                continue
            elif user_data_input_method is UserDataInputMethod.ROLE:
                error_message = None
                assert isinstance(user_input, UserRole)
                user_role = user_input
                user_data_input_method = UserDataInputMethod.PASSWORD
                continue
            elif user_data_input_method is UserDataInputMethod.PASSWORD:
                error_message = None
                assert isinstance(user_input, str)
                assert isinstance(user_name, str)
                assert isinstance(user_role, UserRole)
                user_password = user_input
                assert isinstance(user_password, str)

                new_user = User(name=user_name,
                                role=user_role,
                                password=user_password)

                add_user(new_user)

            break