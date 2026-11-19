from classes.product import Product
from classes.table_column import Column
from components.render_table import render_table
from utils.get_table_width import get_table_width


def products_table(
        data: list[Product],
        starting_row: int,
        selected: list[Product] | None = None,
        summary: str | None = None
):
    columns: list[Column] = [
        Column(
            header="CENA",
            key="price",
            width=9,
            decorator=" zł"
        )
    ]

    render_table(
        data=data,
        starting_row=starting_row,
        left_header="NAZWA",
        left_key="name",
        columns=columns,
        selected=selected,
        addon_row_header="SUMA" if summary else None,
        addon_row_value=summary
    )