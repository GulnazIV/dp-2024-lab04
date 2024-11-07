from interfaces import BaseAnalogClock
from consts import DayNightDivision


class AnalogClock(BaseAnalogClock):
    """
    Класс, реализующий аналоговые часы.
    """

    def __init__(self):
        """
        Инициализирует новый экземпляр класса AnalogClock с начальными значениями.
        """
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour_angle = 0.0
        self.minute_angle = 0.0
        self.second_angle = 0.0
        self.day_night_division = DayNightDivision.AM

    def set_date_time(
        self,
        year: int,
        month: int,
        day: int,
        hour_angle: float,
        minute_angle: float,
        second_angle: float,
        day_night_division: DayNightDivision,
    ):
        """
        Устанавливает дату и время для аналоговых часов.

        :param year: Год.
        :param month: Месяц.
        :param day: День месяца.
        :param hour_angle: Угол часовой стрелки в градусах.
        :param minute_angle: Угол минутной стрелки в градусах.
        :param second_angle: Угол секундной стрелки в градусах.
        :param day_night_division: Переменная, обозначающая текущее время суток.
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        """
        Возвращает текущий угол часовой стрелки.
        """
        return self.hour_angle

    def get_minute_angle(self) -> float:
        """
        Возвращает текущий угол минутной стрелки.
        """
        return self.minute_angle

    def get_second_angle(self) -> float:
        """
        Возвращает текущий угол секундной стрелки.
        """
        return self.second_angle

    def get_year(self) -> int:
        """
        Возвращает год.
        """
        return self.year

    def get_month(self) -> int:
        """
        Возвращает месяц.
        """
        return self.month

    def get_day(self) -> int:
        """
        Возвращает день.
        """
        return self.day
