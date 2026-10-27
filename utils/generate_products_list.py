import json
from pathlib import Path

from utils.admin.get_products_list_path import get_products_list_path
from utils.admin.get_users_list_path import get_users_list_path
from utils.terminal import clear_screen, move_cursor, write

def default_json_dump(path: Path):
    users = [{
        "name": "Przykladowy produkt",
        "price": 24.00
    }]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def generate_products_list():
    clear_screen()

    list_path = get_products_list_path()

    try:
        with open(list_path, "r", encoding="utf-8") as f:
            json.load(f)

    except FileNotFoundError:
        move_cursor(2)
        write("Tworzenie plików...")

        list_path.parent.mkdir(parents=True, exist_ok=True)

        default_json_dump(list_path)

    except json.JSONDecodeError as e:
        move_cursor(2)
        write("Lista produktów jest uszkodzona")
        move_cursor(3)
        write("Wykonuję kopię zapasową do pliku:")

        corrupted_path = list_path.with_suffix(".json.corrupted")
        list_path.rename(corrupted_path)

        move_cursor(4)
        write(corrupted_path.absolute().as_posix())

        default_json_dump(list_path)
