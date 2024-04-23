from enum import Enum


class CardStatus(Enum):
    OPEN = 'open'
    CANCELED = 'canceled'
    COMPLETED = 'completed'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

    @classmethod
    def get_complete_choices(cls):
        return [(item.name, item.name) for item in cls]
