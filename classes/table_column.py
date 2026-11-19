from classes.table_column_variant import ColumnVariant


class Column:
    def __init__(
            self,
            header: str,
            key: str,
            width: int,
            decorator: str | None = None,
            numbers_with_precision: bool | None = True,
            variant: ColumnVariant | None = ColumnVariant.NUMBER
    ):
        self.header = header
        self.key = key
        self.width = width
        self.decorator = decorator
        self.numbers_with_precision = numbers_with_precision
        self.variant = variant
