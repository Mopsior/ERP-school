from typing import Callable

class MenuOption:
    def __init__(self, name: str, fun: Callable):
        self.name = name
        self.fun = fun

    def execute(self):
        return self.fun()