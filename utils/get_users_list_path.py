from pathlib import Path

from utils.config import user_list_file_path

def get_users_list_path() -> Path:
    base_dir = Path(__file__).resolve().parent.parent
    relative_file_path = base_dir / user_list_file_path

    return relative_file_path