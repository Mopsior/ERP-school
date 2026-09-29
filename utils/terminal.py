import sys

def write(content):
    sys.stdout.write(content)
    sys.stdout.flush()


def clear_screen():
    # \033[2J - czyści ekran, \033[H - ustawia kursor na pozycji (1,1)
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()


def move_cursor(row: int, col: int | None = 1):
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()


def from_bottom(all_rows: int, row: int) -> int:
    return all_rows - row