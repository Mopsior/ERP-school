from enum import Enum


class PromotionInputMethod(Enum):
    NAME = 'name',
    PERCENTAGE = 'percentage',
    ACTIVE = 'active',
    CONFIRMATION = 'confirmation'