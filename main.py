# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from components.runtime_file_error import runtime_file_error
from utils.generate_users_list import generate_users_list
from utils.terminal import clear_screen, write, move_cursor
from modules.select_module import select_module

def main():
    try:
        generate_users_list()
        select_module()
    except KeyboardInterrupt:
        clear_screen()
        sys.exit()
    except FileNotFoundError:
        runtime_file_error()
        sys.exit()

if __name__ == '__main__':
    main()