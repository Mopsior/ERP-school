import json
import os

from classes.product import Product
from utils.admin.get_products_list_path import get_products_list_path
from utils.admin.get_users_list_path import get_users_list_path
from utils.terminal import move_cursor, write
from classes.user import User


def get_products() -> list[Product] | None:
    list_path = get_products_list_path()
    columns, rows = os.get_terminal_size()

    try:
        with open(list_path, "r", encoding="utf-8") as f:
            products: list[Product] = json.load(f)
            return products
    except (FileNotFoundError, json.JSONDecodeError):
        move_cursor(columns - 2)
        write("BŁĄD: Nie można otworzyć pliku z produktami")
        move_cursor(columns - 1)
        write("Uruchom program ponownie, aby naprawić błąd")