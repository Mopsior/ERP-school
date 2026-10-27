import json

from modules.admin.user_details import user_details
from utils.admin.get_users import get_users
from utils.admin.get_users_list_path import get_users_list_path
from classes.user import User


def add_user(new_user: User) -> None:
    users = get_users()
    if not users: raise FileNotFoundError

    list_path = get_users_list_path()

    users.append(new_user)

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    user_details(len(users) - 1)
    return