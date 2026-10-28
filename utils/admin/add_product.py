import json

from classes.product import Product
from modules.admin.product_details import product_details
from utils.admin.get_products import get_products
from utils.admin.get_products_list_path import get_products_list_path


def add_product(new_product: Product) -> None:
    products = get_products()

    list_path = get_products_list_path()

    if not products:
        products = [new_product]
    else:
        products.append(new_product)

    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    product_details(len(products) - 1)
    return