from datetime import datetime

from interfaces.base_analog_clock import BaseAnalogClock
from interfaces.base_digital_clock import BaseDigitalClock

from clocks.time_converter import TimeConverter


class DigitalClockAdapter(BaseDigitalClock):
    """
    Адаптер для преобразования аналоговых часов в цифровые.
    """

    def __init__(self, analog_clock: BaseAnalogClock):
        """
        Инициализирует новый экземпляр DigitalClockAdapter и создает экземпляр AnalogClock.

        :param analog_clock: Экземпляр аналоговых часов для адаптации.
        """
        self._analog_clock = analog_clock

    def set_date_time(self, date: datetime):
        """
        Устанавливает дату и время для аналоговых часов в формате datetime.

        :param date: Объект datetime, содержащий дату и время.
        """
        hour_angle, minute_angle, second_angle, day_night_division = (
            TimeConverter.convert_time_to_angles(date.hour, date.minute, date.second)
        )
        self._analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=hour_angle,
            minute_angle=minute_angle,
            second_angle=second_angle,
            day_night_division=day_night_division,
        )

    def get_date_time(self) -> datetime:
        """
        Возвращает время в формате datetime на основе аналоговых часов.

        :return Дату и время в формате datetime.
        """
        year = self._analog_clock.get_year()
        month = self._analog_clock.get_month()
        day = self._analog_clock.get_day()
        hour, minute, second = TimeConverter.convert_angles_to_time(
            self._analog_clock.get_hour_angle(),
            self._analog_clock.get_minute_angle(),
            self._analog_clock.get_second_angle(),
            self._analog_clock.day_night_division,
        )
        return datetime(year, month, day, hour, minute, second)
