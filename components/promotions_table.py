from classes.product import Product
from classes.promotion import Promotion
from classes.table_column import Column
from classes.table_column_variant import ColumnVariant
from components.render_table import render_table
from utils.get_table_width import get_table_width


def promotions_table(data: list[Promotion], starting_row: int):
    columns = [
        Column(
            header="ZNIŻKA",
            key="percentage",
            numbers_with_precision=False,
            decorator=" %",
            width=9
        ),
        Column(
            header="AKTYWNE",
            key="active",
            variant=ColumnVariant.BOOL,
            width=3
        )
    ]

    render_table(
        data=data,
        starting_row=starting_row,
        left_header="NAZWA",
        left_key="name",
        columns=columns
    )