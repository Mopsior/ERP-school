import json

from classes.input_mode import AdminInputMode
from utils.admin.get_products import get_products
from utils.admin.get_products_list_path import get_products_list_path


def remove_product(product_id: int) -> None:
    from modules.admin.products import products_list

    products = get_products()
    if not products: raise FileNotFoundError

    list_path = get_products_list_path()

    products.pop(product_id)

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    products_list(AdminInputMode.PAGE_CONTENT)
    return