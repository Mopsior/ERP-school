import os


min_table_width = 32
max_table_width = 120

def get_table_width() -> int:
    columns, rows = os.get_terminal_size()
    columns -= 6

    if columns < min_table_width:
        return min_table_width

    if columns > max_table_width:
        return max_table_width

    return columns