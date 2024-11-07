from dataclasses import dataclass
from consts.date_consts import DayNightDivision


@dataclass
class Time:
    """
    Дата класс для хранения часов, минут, секунд.

    Атрибуты:
        hour (int): Часы.
        minute (int): Минуты.
        second (int): Секунды.
    """

    hour: int
    minute: int
    second: int
