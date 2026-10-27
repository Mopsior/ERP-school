import json

from classes.input_mode import AdminInputMode
from utils.admin.get_users import get_users
from utils.admin.get_users_list_path import get_users_list_path


def remove_user(user_id: int):
    from modules.admin.admin import admin
    users = get_users()
    if not users: raise FileNotFoundError

    list_path = get_users_list_path()

    users.pop(user_id)

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    admin(AdminInputMode.PAGE_CONTENT)
    return