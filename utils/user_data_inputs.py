from classes.menu_option import MenuOption
from classes.user_role import UserRole
from utils.int_input import int_input


def user_name_input() -> str:
    user_input = input().strip()

    if len(user_input) <= 0:
        raise TypeError('Nazwa użytkownika jest za krótka')

    if len(user_input) >= 64:
        raise TypeError('Nazwa użytkownika jest za długa')

    return user_input

def user_role_input(roles_list: list[MenuOption]) -> UserRole:
    try:
        user_input = int_input(None)

        if user_input is None:
            raise TypeError

        if user_input <= 0:
            raise IndexError

        selected_option = roles_list[user_input - 1]
    except (ValueError, TypeError):
        raise TypeError('To nie jest liczba! Wprowadź opcje ponownie')
    except IndexError:
        raise TypeError(f'Nie ma opcji nr {user_input}')
    else:
        assert isinstance(selected_option.data, UserRole)
        return selected_option.data

def user_password_input() -> str:
    user_input = input().strip()

    if len(user_input) <= 0:
        raise TypeError('Hasło jest za krótka')

    if len(user_input) >= 128:
        raise TypeError('Hasło jest za długa')

    return user_input