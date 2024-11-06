from datetime import datetime

from consts.date_consts import DayNightDivision
from interfaces.base_analog_clock import BaseAnalogClock
from interfaces.base_digital_clock import BaseDigitalClock

from consts.time_consts import TimeConsts


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
            self._convert_time_to_angles(date.hour, date.minute, date.second)
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
        hour, minute, second = self._convert_angles_to_time()
        return datetime(year, month, day, hour, minute, second)

    def _convert_time_to_angles(
        self, hour: int, minute: int, second: int
    ) -> tuple[float, float, float, DayNightDivision]:
        """
        Преобразует часы, минуты, секунды в углы для аналоговых часов.

        :param hour: Часы.
        :param minute: Минуты.
        :param second: Секунды.
        """
        hour_angle = (hour % TimeConsts.HOURS) * TimeConsts.HOUR_TO_DEGREES + (
            minute / TimeConsts.MINUTES
        ) * TimeConsts.HOUR_TO_DEGREES
        minute_angle = minute * TimeConsts.MINUTE_TO_DEGREES
        second_angle = second * TimeConsts.SECOND_TO_DEGREES
        day_night_division = (
            DayNightDivision.AM.value
            if hour < TimeConsts.MIDDLE_DAY
            else DayNightDivision.PM.value
        )
        return hour_angle, minute_angle, second_angle, day_night_division

    def _convert_angles_to_time(self):
        """
        Преобразует углы часов, минут, секунд.

        :return Преобразованные часы, минуты, секунды.
        """
        hour = (
            self._analog_clock.get_hour_angle() // TimeConsts.HOUR_TO_DEGREES
        ) % TimeConsts.HOURS
        if (
            self._analog_clock.day_night_division == DayNightDivision.PM.value
            and hour != TimeConsts.MIDDLE_DAY
        ):
            hour += TimeConsts.HOURS
        elif (
            self._analog_clock.day_night_division == DayNightDivision.AM.value
            and hour == TimeConsts.MIDDLE_DAY
        ):
            hour = hour
        minute = self._analog_clock.get_minute_angle() // TimeConsts.MINUTE_TO_DEGREES
        second = self._analog_clock.get_second_angle() // TimeConsts.SECOND_TO_DEGREES
        return int(hour), int(minute), int(second)
