import json
import os

from utils.get_users_list_path import get_users_list_path
from utils.terminal import move_cursor, write
from classes.user import User


def get_users() -> list[User] | None:
    list_path = get_users_list_path()
    columns, rows = os.get_terminal_size()

    try:
        with open(list_path, "r", encoding="utf-8") as f:
            users: list[User] = json.load(f)
            return users
    except (FileNotFoundError, json.JSONDecodeError):
        move_cursor(columns - 2)
        write("BŁĄD: Nie można otworzyć pliku z listą użytkowników")
        move_cursor(columns - 1)
        write("Uruchom program ponownie, aby naprawić błąd")