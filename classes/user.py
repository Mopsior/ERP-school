from typing import TypedDict

from classes.user_role import UserRole


class User(TypedDict):
    name: str
    password: str
    role: UserRole