# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

class MenuOption:
    def __init__(self, name):
        self.name = name


def write(content):
    sys.stdout.write(content)
    sys.stdout.flush()


def clear_screen():
    # \033[2J - czyści ekran, \033[H - ustawia kursor na pozycji (1,1)
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()


def move_cursor(row: int, col: int):
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()


def get_available_options(length: int):
    available_options = ''
    for i in range(length):
        if i < (length - 1):
            available_options += f'{i+1}, '
        else:
            available_options += str(i+1)
    return available_options


def select_module():
    options = [
        MenuOption('POS'),
        MenuOption('Panel Administracyjny')
    ]
    clear_screen()
    columns, rows = os.get_terminal_size()
    move_cursor(1, 1)
    write('System ERP')
    move_cursor(3, 1)
    write('Wybierz odpowiedni moduł aplikacji:\n1. Wybierz liczbę z listy poniżej\n2. Naciśnij przycisk Enter')
    move_cursor(rows - len(options) + 1, 1)
    write('Wybierz moduł:')

    for i, option in enumerate(options):
        move_cursor(rows - (len(options) - i), 1)
        write(f'({i}) {option.name}')

    move_cursor(rows, 1)
    write(f'Wprwoadź liczbę: ({get_available_options(len(options))}) ')
    user_content = input()

def main():
    try:
        select_module()
    except KeyboardInterrupt:
        clear_screen()
        sys.exit()


if __name__ == '__main__':
    main()