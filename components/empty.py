from utils.chars import top_left, vertical_line, bottom_left, horizontal_line, top_right, bottom_right
from utils.terminal import move_cursor, write


def empty(starting_row: int, content: str) -> None:
    first_line =(
        top_left
        # len(content) + <marings>
        + horizontal_line * (len(content) + 2)
        + top_right
    )
    second_line = f"{vertical_line} " + content + f" {vertical_line}"
    third_line = (
        bottom_left
        + horizontal_line * (len(content) + 2)
        + bottom_right
    )

    move_cursor(starting_row)
    write(first_line)
    move_cursor(starting_row + 1)
    write(second_line)
    move_cursor(starting_row + 2)
    write(third_line)

