from classes.menu_option import MenuOption
from utils.int_input import int_input


def promotion_name_input(default_value: str | None = None) -> str:
    user_input: str = input().strip()
    user_input = default_value if default_value is not None and not user_input else user_input

    if len(user_input) <= 0:
        raise TypeError("Nazwa promocji jest za krótka")

    if len(user_input) > 64:
        raise TypeError("Nazwa promocji jest za długa")

    return user_input

def promotion_percentage_input(default_value: float | None = None) -> float:
    try:
        user_input = input().strip()
        partitioned_input = user_input.replace(',', '.').partition('.')
        if len(partitioned_input[2]) > 2:
            user_input = partitioned_input[0] + partitioned_input[1] + partitioned_input[2][:2]

        user_input = default_value if default_value is not None and not user_input else user_input

        user_input = float(user_input)

        if user_input is None:
            raise ValueError("Nie podano procentu rabatu")

        if user_input < 0:
            raise ValueError("Procent rabatu jest za krótki")

        if user_input > 100:
            raise ValueError("Procent rabatu jest za duży. Maksymalny procent to: 100")

        return user_input
    except TypeError:
        raise TypeError('To nie jest liczba!')
    except ValueError as e:
        raise e

def promotion_active_input(default_value: bool | None = None) -> bool:
    user_input = input().strip().lower()
    user_input = default_value if default_value is not None and not user_input else user_input

    if user_input in ['t', 'tak', 'y', 'yes'] or user_input is True if default_value is not None else False:
        return True
    elif user_input in ['n', 'nie', 'no'] or user_input is False if default_value is not None else False:
        return False
    else:
        raise ValueError("Niepoprawna wartość. Wprowadź 't'/'tak' lub 'n'/'nie'.")