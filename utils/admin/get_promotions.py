import json
import os

from classes.product import Product
from classes.promotion import Promotion
from utils.admin.get_products_list_path import get_products_list_path
from utils.admin.get_promotions_list_path import get_promotions_list_path
from utils.admin.get_users_list_path import get_users_list_path
from utils.terminal import move_cursor, write
from classes.user import User


def get_promotions() -> list[Promotion] | None:
    list_path = get_promotions_list_path()
    columns, rows = os.get_terminal_size()

    try:
        with open(list_path, "r", encoding="utf-8") as f:
            promotions: list[Promotion] = json.load(f)
            return promotions
    except (FileNotFoundError, json.JSONDecodeError):
        move_cursor(columns - 2)
        write("BŁĄD: Nie można otworzyć pliku z promocjami")
        move_cursor(columns - 1)
        write("Uruchom program ponownie, aby naprawić błąd")