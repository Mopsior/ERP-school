
from classes.table_column import Column
from classes.table_column_variant import ColumnVariant
from components.empty import empty
from utils.chars import (
    top_left, horizontal_line, top_right, vertical_line,
    join_left, join_right, intersection, join_top,
    bottom_right, bottom_left, join_bottom, invert_text,
    checkmark, crossmark,
)
from utils.get_table_width import get_table_width
from utils.terminal import move_cursor, write, clear_screen


def render_table(
    data: list,
    starting_row: int,
    left_header: str,
    left_key: str,
    columns: list[Column],
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

    def format_value(value, column: Column) -> str:
        if column.variant == ColumnVariant.BOOL:
            return checkmark if value else crossmark

        if column.variant == ColumnVariant.NUMBER and isinstance(value, (int, float)):
            formatted_value = (
                f"{value:.2f}"
                if column.numbers_with_precision
                else str(value)
            )

            return formatted_value + (column.decorator or "")

        return str(value)

    column_widths = []

    for column in columns:
        max_value_width = max(
            (
                len(format_value(item[column.key], column))
                for item in data
            ),
            default=0
        )

        width = max(
            column.width,
            len(column.header) + 3,
            max_value_width + 3
        )

        if has_addon_row and column is columns[-1]:
            width = max(width, len(addon_row_value) + 3)

        column_widths.append(width)

    column_positions = []
    current_position = table_width

    for width in reversed(column_widths):
        current_position -= width
        column_positions.insert(0, current_position)

    right_starting_width = (
        column_positions[0]
        if column_positions
        else table_width
    )

    min_left_width = len(left_header) + 3

    if right_starting_width - left_starting_width < min_left_width:
        empty("Okno terminala jest za małe, aby wyświetlić tabelę")
        return

    max_name_width = (
        right_starting_width - left_starting_width - 3
    )

    def truncate_left(value: str) -> str:
        if len(value) <= max_name_width:
            return value

        if max_name_width <= 3:
            return value[:max_name_width]

        return value[:max_name_width - 3] + "..."

    def write_columns(row: int, item: dict):
        for column, position, width in zip(
                columns, column_positions, column_widths
        ):
            value = format_value(item[column.key], column)

            content_width = width - 3
            aligned_value = value.rjust(content_width)

            move_cursor(row, position)
            write(f"{vertical_line} {aligned_value} ")

    def write_column_connectors(row: int, connector: str):
        for position in column_positions:
            move_cursor(row, position)
            write(connector)

    move_cursor(starting_row)
    write(top_left + horizontal_line * (table_width - 2) + top_right)

    move_cursor(starting_row, left_starting_width)
    write(join_top)

    write_column_connectors(starting_row, join_top)

    current_row = starting_row + 1

    move_cursor(current_row)
    write(f"{vertical_line} {' ' * index_width} ")

    move_cursor(current_row, left_starting_width)
    write(f"{vertical_line} {left_header} ")

    for column, position in zip(columns, column_positions):
        move_cursor(current_row, position)
        write(f"{vertical_line} {column.header} ")

    move_cursor(current_row, table_width)
    write(vertical_line)

    current_row += 1

    move_cursor(current_row)
    write(join_left + horizontal_line * (table_width - 2) + join_right)

    move_cursor(current_row, left_starting_width)
    write(intersection)

    write_column_connectors(current_row, intersection)

    current_row += 1

    for i, item in enumerate(data, start=1):
        is_selected = item in selected if selected else False

        move_cursor(current_row)

        index = f"{i:>{index_width}}"

        if is_selected:
            index = invert_text(index)

        write(f"{vertical_line} {index} ")

        move_cursor(current_row, left_starting_width)

        parsed_name = truncate_left(str(item[left_key]))

        write(f"{vertical_line} {parsed_name} ")

        write_columns(current_row, item)

        move_cursor(current_row, table_width)
        write(vertical_line)

        current_row += 1

    if has_addon_row:
        move_cursor(current_row)
        write(join_left + horizontal_line * (table_width - 2) + join_right)

        if columns:
            move_cursor(current_row, column_positions[-1])
            write(intersection)

        current_row += 1

        move_cursor(current_row)
        write(f"{vertical_line} {addon_row_header} ")

        if columns:
            content_width = column_widths[-1] - 3
            aligned_value = addon_row_value.rjust(content_width)

            move_cursor(current_row, column_positions[-1])
            write(f"{vertical_line} {aligned_value} ")

        move_cursor(current_row, table_width)
        write(vertical_line)

        current_row += 1

    move_cursor(current_row)
    write(bottom_left + horizontal_line * (table_width - 2) + bottom_right)

    if not has_addon_row:
        move_cursor(current_row, left_starting_width)
        write(join_bottom)

        write_column_connectors(current_row, join_bottom)

    elif columns:
        move_cursor(current_row, column_positions[-1])
        write(join_bottom)
