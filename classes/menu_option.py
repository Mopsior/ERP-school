from typing import Callable, Any


class MenuOption:
    def __init__(self, name: str, fun: Callable | None = None, data: Any | None = None, hidden_from_list: bool = False, hidden_from_tabs: bool = False, selected: bool = False):
        self.name = name
        self.fun = fun
        self.data = data
        self.hidden_from_list = hidden_from_list
        self.hidden_from_tabs = hidden_from_tabs
        self.selected = selected

    def execute(self):
        return self.fun()