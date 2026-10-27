from classes.menu_option import MenuOption
from classes.user_role import UserRole


def get_role_index(all_roles: list[MenuOption], role: UserRole) -> int:
    return next(
        (i for i, option in enumerate(all_roles)
         if option.data == role),
        -1
    )