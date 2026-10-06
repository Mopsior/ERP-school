from classes.user import User
from utils.chars import top_left, horizontal_line, top_right, vertical_line, join_left, join_right, intersection, \
    join_top, join_bottom, bottom_right, bottom_left
from utils.terminal import move_cursor, write


table_width = 48
role_starting_width = table_width - 9
# - 7 because 3 chars are decorators, 4 are spaces
max_name_width = role_starting_width - 7

def user_table(data: list[User], starting_row: int):
    move_cursor(starting_row)
    write(top_left + horizontal_line * (table_width - 2 ) + top_right)

    move_cursor(starting_row, role_starting_width)
    write(join_top)

    current_row = starting_row + 1

    move_cursor(current_row)
    write(f"{vertical_line} NAZWA")

    move_cursor(current_row, role_starting_width)
    write(f"{vertical_line} ROLA")

    move_cursor(current_row, table_width)
    write(vertical_line)

    current_row += 1

    move_cursor(current_row)
    write(join_left + horizontal_line * (table_width - 2) + join_right)

    move_cursor(current_row, role_starting_width)
    write(intersection)

    current_row += 1
    for i, user in enumerate(data):
        move_cursor(current_row)
        parsed_user_name = user["name"]
        if len(parsed_user_name) >= max_name_width:
            parsed_user_name = parsed_user_name[0:max_name_width]
            parsed_user_name += "..."

        write(f"{vertical_line} {parsed_user_name}")

        move_cursor(current_row, role_starting_width)
        write(f"{vertical_line} {user["role"]}")

        move_cursor(current_row, table_width)
        write(vertical_line)
        current_row += 1

    move_cursor(current_row)
    write(bottom_left + horizontal_line * (table_width - 2) + bottom_right)

    move_cursor(current_row, role_starting_width)
    write(join_bottom)