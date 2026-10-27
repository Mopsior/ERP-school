
from utils.chars import (
    top_left, horizontal_line, top_right, vertical_line,
    join_left, join_right, intersection, join_top,
    join_bottom, bottom_right, bottom_left,
)
from utils.get_table_width import get_table_width
from utils.terminal import move_cursor, write


def render_table(
    data: list,
    starting_row: int,
    left_header: str,
    left_key: str,
    right_header: str,
    right_key: str,
    right_starting_width: int,
):
    table_width = get_table_width()
    index_width = len(str(len(data)))
    left_starting_width = index_width + 4
    max_name_width = right_starting_width - left_starting_width - 5

    move_cursor(starting_row)
    write(top_left + horizontal_line * (table_width - 2) + top_right)

    move_cursor(starting_row, left_starting_width)
    write(join_top)

    move_cursor(starting_row, right_starting_width)
    write(join_top)

    current_row = starting_row + 1

    move_cursor(current_row)
    write(f"{vertical_line} {' ' * index_width}")

    move_cursor(current_row, left_starting_width)
    write(f"{vertical_line} {left_header}")

    move_cursor(current_row, right_starting_width)
    write(f"{vertical_line} {right_header}")

    move_cursor(current_row, table_width)
    write(vertical_line)

    current_row += 1

    move_cursor(current_row)
    write(join_left + horizontal_line * (table_width - 2) + join_right)

    move_cursor(current_row, left_starting_width)
    write(intersection)

    move_cursor(current_row, right_starting_width)
    write(intersection)

    current_row += 1

    for i, item in enumerate(data, start=1):
        move_cursor(current_row)
        write(f"{vertical_line} {i:>{index_width}} ")

        move_cursor(current_row, left_starting_width)
        parsed_name = item[left_key]

        if len(parsed_name) >= max_name_width:
            parsed_name = parsed_name[0:max_name_width]
            parsed_name += "..."

        write(f"{vertical_line} {parsed_name}")

        move_cursor(current_row, right_starting_width)
        value = item[right_key]

        if isinstance(value, (int, float)):
            value = f"{value:.2f}"

        write(f"{vertical_line} {value}")

        move_cursor(current_row, table_width)
        write(vertical_line)

        current_row += 1

    move_cursor(current_row)
    write(bottom_left + horizontal_line * (table_width - 2) + bottom_right)

    move_cursor(current_row, left_starting_width)
    write(join_bottom)

    move_cursor(current_row, right_starting_width)
    write(join_bottom)
