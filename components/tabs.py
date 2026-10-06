from classes.menu_option import MenuOption
from utils.chars import invert_text, vertical_line, horizontal_line, top_connector, bottom_right
from utils.terminal import move_cursor, write


def tabs(options: list[MenuOption]):
    first_line:str = " "
    second_line: str = ""

    for i, option in enumerate(options):
        first_line += invert_text(options[i].name) if i is 0 else options[i].name
        first_line += f' {vertical_line} '

        second_line += horizontal_line * (len(option.name) + 2)
        second_line += top_connector if i < (len(options) - 1) else bottom_right

    move_cursor(1)
    write(first_line),
    move_cursor(2)
    write(second_line)