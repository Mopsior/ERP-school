def promotion_name_input() -> str:
    user_input: str = input().strip()

    if len(user_input) <= 0:
        raise TypeError("Nazwa promocji jest za krótka")

    if len(user_input) > 64:
        raise TypeError("Nazwa promocji jest za długa")

    return user_input

def promotion_percentage_input() -> float:
    try:
        user_input = input().strip()
        partitioned_input = user_input.replace(',', '.').partition('.')
        if len(partitioned_input[2]) > 2:
            user_input = partitioned_input[0] + partitioned_input[1] + partitioned_input[2][:2]

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