from classes.product import Product
from components.render_table import render_table
from utils.get_table_width import get_table_width


def products_table(data: list[Product], starting_row: int, selected: list[Product] | None = None, summary: str | None = None):
    table_width = get_table_width()
    price_starting_width = table_width - 9

    render_table(
        data=data,
        starting_row=starting_row,
        left_header="NAZWA",
        left_key="name",
        right_header="CENA",
        right_key="price",
        right_starting_width=price_starting_width,
        selected=selected,
        addon_row_header="SUMA" if summary else None,
        addon_row_value=summary
    )