import json

from classes.product import Product
from modules.admin.product_details import product_details
from utils.admin.get_products import get_products
from utils.admin.get_products_list_path import get_products_list_path


def edit_product(updated_product: Product, product_id: int) -> None:
    products = get_products()

    list_path = get_products_list_path()

    products[product_id] = updated_product

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    product_details(product_id)
    return