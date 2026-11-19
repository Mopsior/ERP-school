from classes.table_column import Column
from classes.user import User
from components.render_table import render_table
from utils.chars import top_left, horizontal_line, top_right, vertical_line, join_left, join_right, intersection, \
    join_top, join_bottom, bottom_right, bottom_left
from utils.get_table_width import get_table_width
from utils.terminal import move_cursor, write


def user_table(data: list[User], starting_row: int):
    columns: list[Column] = [
        Column(
            header="ROLA",
            key="role",
            width=9
        )
    ]

    render_table(
        data=data,
        starting_row=starting_row,
        left_header="NAZWA",
        left_key="name",
        columns=columns
    )