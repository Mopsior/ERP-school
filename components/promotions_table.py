from classes.product import Product
from classes.promotion import Promotion
from components.render_table import render_table
from utils.get_table_width import get_table_width


def promotions_table(data: list[Promotion], starting_row: int):
    table_width = get_table_width()
    promotion_starting_width = table_width - 9

    render_table(
        data=data,
        starting_row=starting_row,
        left_header="NAZWA",
        left_key="name",
        right_header="ZNIŻKA",
        right_key="percentage",
        right_with_precision=False,
        right_decorator=" %",
        right_starting_width=promotion_starting_width
    )