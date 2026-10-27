from pathlib import Path

from utils.config import user_list_file_path, products_list_file_path


def get_products_list_path() -> Path:
    base_dir = Path(__file__).resolve().parent.parent.parent
    relative_file_path = base_dir / products_list_file_path

    return relative_file_path