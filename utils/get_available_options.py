from utils.chars import invert_text


def get_available_options(length: int, selected: int | None = None):
    available_options = ''
    for i in range(length):
        if i < (length - 1):
            available_options += f'{invert_text(str(i + 1))}, ' if selected is i else f'{i+1}, '
        else:
            available_options += invert_text(str(i+1)) if selected is i else str(i+1)
    return available_options