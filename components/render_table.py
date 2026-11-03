from utils.chars import (
    top_left, horizontal_line, top_right, vertical_line,
    join_left, join_right, intersection, join_top,
    join_bottom, bottom_right, bottom_left, invert_text,
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
    selected: list | None = None,
    addon_row_header: str | None = None,
    addon_row_value: str | None = None
):
    table_width = get_table_width()
    index_width = len(str(len(data)))
    left_starting_width = index_width + 4

    has_addon_row = (
        addon_row_header is not None
        and addon_row_value is not None
    )

    if has_addon_row and addon_row_value:
        right_starting_width = min(
            right_starting_width,
            table_width - max(
                len(right_header),
                len(addon_row_value)
            ) - 3
        )

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
        is_selected = item in selected if selected else False

        move_cursor(current_row)

        index = f"{i:>{index_width}}"
        if is_selected:
            index = invert_text(index)

        write(f"{vertical_line} {index} ")

        move_cursor(current_row, left_starting_width)
        parsed_name = str(item[left_key])

        if len(parsed_name) > max_name_width:
            parsed_name = parsed_name[:max_name_width] + "..."

        write(f"{vertical_line} {parsed_name}")

        move_cursor(current_row, right_starting_width)
        value = item[right_key]

        if isinstance(value, (int, float)):
            value = f"{value:.2f}"

        write(f"{vertical_line} {value}")

        move_cursor(current_row, table_width)
        write(vertical_line)

        current_row += 1

    if has_addon_row:
        move_cursor(current_row)
        write(join_left + horizontal_line * (table_width - 2) + join_right)

        move_cursor(current_row, right_starting_width)
        write(intersection)

        current_row += 1

        move_cursor(current_row)
        write(f"{vertical_line} {addon_row_header}")

        move_cursor(current_row, right_starting_width)
        write(f"{vertical_line} {addon_row_value}")

        move_cursor(current_row, table_width)
        write(vertical_line)

        current_row += 1

    move_cursor(current_row)
    write(bottom_left + horizontal_line * (table_width - 2) + bottom_right)

    if not has_addon_row and not has_addon_row:
        move_cursor(current_row, left_starting_width)
        write(join_bottom)

    move_cursor(current_row, right_starting_width)
    write(join_bottom)