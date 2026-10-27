from classes.menu_option import MenuOption
from classes.user_role import UserRole
from utils.config import required_symbols, required_numbers
from utils.get_role_index import get_role_index
from utils.int_input import int_input


def user_name_input(default_value: str | None = None) -> str:
    user_input = input().strip()
    user_input = default_value if default_value is not None and not user_input else user_input

    if len(user_input) <= 0:
        raise TypeError('Nazwa użytkownika jest za krótka')

    if len(user_input) >= 64:
        raise TypeError('Nazwa użytkownika jest za długa')

    return user_input

def user_role_input(roles_list: list[MenuOption], default_value: UserRole | None = None) -> UserRole:
    default_value_index: int | None = get_role_index(roles_list, default_value) if default_value else None

    try:
        user_input = int_input(None)

        if user_input is None and default_value is not None:
            selected_option = roles_list[default_value_index]
            assert isinstance(selected_option.data, UserRole)
            return selected_option.data

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

    if len(user_input) <= 8:
        raise TypeError('Hasło jest za krótka. Minimalna długość to 8 znaków')

    if len(user_input) >= 128:
        raise TypeError('Hasło jest za długa. Maksymalna długość to 128 znaków')

    if not any(char.isdigit() for char in user_input):
        raise TypeError("Hasło musi mieć co najmniej jedną liczbę")

    # czy dowolny symbol w tekscie użytkownika dla symbolu z required_symbols
    if not any(symbol in user_input for symbol in required_symbols):
        raise TypeError("Hasło musi mieć co najmniej jeden symbol")

    return user_input

def user_confirmation_input(options: list[MenuOption]) -> bool:
    try:
        user_input = int_input(None)

        if user_input is None:
            raise TypeError

        if user_input <= 0:
            raise IndexError

        selected_option = options[user_input - 1]
    except (ValueError, TypeError):
        raise TypeError('To nie jest liczba! Wprowadź opcje ponownie')
    except IndexError:
        raise TypeError(f'Nie ma opcji nr {user_input}')
    else:
        assert isinstance(selected_option.data, bool)
        return selected_option.data