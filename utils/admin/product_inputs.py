from classes.menu_option import MenuOption
from utils.int_input import int_input


def product_name_input(default_value: str | None = None) -> str:
    user_input: str = input().strip()
    user_input = default_value if default_value is not None and not user_input else user_input

    if len(user_input) <= 0:
        raise TypeError("Nazwa produktu jest za krótka")

    if len(user_input) > 64:
        raise TypeError("Nazwa produktu jest za długa")

    return user_input

def product_price_input(default_value: float | None = None) -> float:
    try:
        user_input = input().strip()
        user_input = default_value if default_value is not None and not user_input else user_input

        user_input = float(user_input)

        if user_input is None:
            raise ValueError("Nie podano ceny produktu")

        if user_input < 0:
            raise ValueError("Cena produktu jest za krótka")

        return user_input
    except TypeError:
        raise TypeError('To nie jest liczba!')
    except ValueError as e:
        raise e

def product_confirmation_input(options: list[MenuOption]) -> bool:
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