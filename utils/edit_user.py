import json

from classes.user import User
from utils.get_users import get_users
from utils.get_users_list_path import get_users_list_path


def edit_user(updated_user: User , user_id: int) -> None:
    from modules.user_details import user_details

    users = get_users()
    if not users: raise FileNotFoundError
    if user_id > (len(users) - 1): raise IndexError

    list_path = get_users_list_path()

    users[user_id] = updated_user

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    user_details(user_id)
    return