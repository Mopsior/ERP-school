import os
from typing import Callable

from classes.login_mode import LoginMode
from classes.user_role import UserRole
from utils.get_users import get_users
from utils.terminal import clear_screen, write, move_cursor, from_bottom


def login(mode: LoginMode, redirect: Callable) -> None:
    users = get_users()
    if not users: raise FileNotFoundError

    user_name: str | None = None
    user_password: str | None = None

    error_message: str | None = None

    while True:
        clear_screen()
        columns, rows = os.get_terminal_size()

        move_cursor(1)
        write("LOGOWANIE")
        move_cursor(2)
        write(f'Do panelu {"Pracownika" if mode is LoginMode.WORKER else "Administratora"}')

        if user_name:
            move_cursor(4)
            write("Nazwa użytkownika:")
            move_cursor(5)
            write(user_name)

        if error_message:
            move_cursor(from_bottom(rows, 3))
            write(error_message)

        move_cursor(from_bottom(rows, 1))

        try:
            if not user_name:
                write("Wpisz nazwę użytkownika:")
                move_cursor(rows)
                user_name = input().strip()
                continue
            else:
                write("Wpisz hasło:")
                move_cursor(rows)
                user_password = input().strip()

                if user_name and user_password:
                    user = next(
                        (
                            user for user in users
                            if user['name'] == user_name and user['password'] == user_password and user['role'] == (UserRole.WORKER.value if mode is LoginMode.WORKER else UserRole.ADMIN.value)
                        ),
                        None
                    )

                    if user is None:
                        raise IndexError

                    redirect()
        except IndexError:
            error_message = "Niepoprawna nazwa użytkownika lub hasło"
        else:
            error_message = None
            break