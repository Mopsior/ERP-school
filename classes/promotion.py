from typing import TypedDict


class Promotion(TypedDict):
    name: str
    percentage: float
    active: bool