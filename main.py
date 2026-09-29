# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from utils.terminal import clear_screen
from modules.select_module import select_module

def main():
    try:
        select_module()
    except KeyboardInterrupt:
        clear_screen()
        sys.exit()


if __name__ == '__main__':
    main()