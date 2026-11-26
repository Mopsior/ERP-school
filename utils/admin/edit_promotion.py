import json

from classes.promotion import Promotion
from modules.admin.promotion_details import promotion_details
from utils.admin.get_promotions import get_promotions
from utils.admin.get_promotions_list_path import get_promotions_list_path


def edit_promotion(updated_promotion: Promotion, promotion_id: int) -> None:
    promotions = get_promotions()

    list_path = get_promotions_list_path()

    promotions[promotion_id] = updated_promotion

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(promotions, f, indent=4, ensure_ascii=False)

    promotion_details(promotion_id)
    return