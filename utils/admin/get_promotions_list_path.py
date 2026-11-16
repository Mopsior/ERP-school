from pathlib import Path

from utils.config import user_list_file_path, products_list_file_path, promotions_list_file_path


def get_promotions_list_path() -> Path:
    base_dir = Path(__file__).resolve().parent.parent.parent
    relative_file_path = base_dir / promotions_list_file_path

    return relative_file_path