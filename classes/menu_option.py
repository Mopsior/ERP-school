from typing import Callable

class MenuOption:
    def __init__(self, name: str, fun: Callable, hidden_from_list: bool = False, hidden_from_tabs: bool = False):
        self.name = name
        self.fun = fun
        self.hidden_from_list = hidden_from_list
        self.hidden_from_tabs = hidden_from_tabs

    def execute(self):
        return self.fun()