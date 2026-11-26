from classes.menu_option import MenuOption
from components.bottom_nav_list import bottom_nav_list
from utils.int_input import int_input
from utils.get_available_options import get_available_options
from utils.terminal import from_bottom, move_cursor, write


def action_selection(
    options: list[MenuOption],
    rows: int,
    prompt: str,
    error_message: str | None = None,
    selected_option: int | None = None,
    visible_options_only: bool = False,
    show_available_options: bool = True
) -> tuple[MenuOption | None, str | None]:
    option_count = (
        sum(not option.hidden_from_list for option in options)
        if visible_options_only
        else len(options)
    )

    move_cursor(from_bottom(rows, option_count + 1))
    write(prompt)
    bottom_nav_list(options, rows)

    if error_message:
        move_cursor(from_bottom(rows, option_count + 3))
        write(error_message)

    move_cursor(rows)
    if show_available_options:
        with_is_return: bool = any(x.is_return for x in options)
        write(f'{"Wprowadź:" if with_is_return else "Wprowadź liczbę:"} ({
        get_available_options(sum(
            1 for option in options if not option.hidden_from_list and not option.is_return),
            selected_option,
            with_is_return
        )}) ')
    else:
        write('Wprwoadź liczbę: ')

    user_input = None
    try:
        user_input = input().strip()

        if user_input == ":q":
            return next((option for option in options if option.is_return), None), None

        user_input = int(user_input)

        if user_input is None:
            raise TypeError

        if user_input <= 0:
            raise IndexError

        return options[user_input - 1], error_message
    except (ValueError, TypeError):
        return None, 'To nie jest liczba! Wprowadź opcje ponownie'
    except IndexError:
        return None, f'Nie ma opcji nr {user_input}'
