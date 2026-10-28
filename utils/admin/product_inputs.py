from utils.int_input import int_input


def product_name_input() -> str:
    user_input: str = input().strip()

    if len(user_input) <= 0:
        raise TypeError("Nazwa produktu jest za krótka")

    if len(user_input) > 64:
        raise TypeError("Nazwa produktu jest za długa")

    return user_input

def product_price_input() -> float:
    try:
        user_input = float(input())
        if user_input is None:
            raise ValueError("Nie podano ceny produktu")

        if user_input < 0:
            raise ValueError("Cena produktu jest za krótka")

        return user_input
    except TypeError:
        raise TypeError('To nie jest liczba!')
    except ValueError as e:
        raise e