import json

from classes.input_mode import AdminInputMode
from utils.admin.get_promotions import get_promotions
from utils.admin.get_promotions_list_path import get_promotions_list_path


def remove_promotion(promotion_id: int) -> None:
    from modules.admin.promotions import promotions_list

    promotions = get_promotions()
    if not promotions: raise FileNotFoundError

    list_path = get_promotions_list_path()

    promotions.pop(promotion_id)

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(promotions, f, indent=4, ensure_ascii=False)

    promotions_list(AdminInputMode.PAGE_CONTENT)
    return