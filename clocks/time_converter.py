from consts.time_consts import TimeConsts
from consts.date_consts import DayNightDivision

from data_classes.time_angles import TimeAngles
from data_classes.time import Time


class TimeConverter:
    """
    Класс для преобразования времени между углами стрелок аналоговых часов и стандартными единицами времени.
    """

    @staticmethod
    def convert_time_to_angles(hour: int, minute: int, second: int) -> TimeAngles:
        """
        Преобразует часы, минуты, секунды в углы для аналоговых часов.

        :param hour: Часы.
        :param minute: Минуты.
        :param second: Секунды.

        :return Преобразованные часы, минуты, секунды и переменная, обозначающая текущее время суток.
        """
        hour_angle = (hour % TimeConsts.ANALOG_HOURS) * TimeConsts.HOUR_TO_DEGREES + (
            minute / TimeConsts.ANALOG_MINUTES
        ) * TimeConsts.HOUR_TO_DEGREES
        minute_angle = minute * TimeConsts.MINUTE_TO_DEGREES
        second_angle = second * TimeConsts.SECOND_TO_DEGREES
        day_night_division = (
            DayNightDivision.AM.value
            if hour < TimeConsts.MIDDLE_DAY
            else DayNightDivision.PM.value
        )
        return TimeAngles(hour_angle, minute_angle, second_angle, day_night_division)

    @staticmethod
    def convert_angles_to_time(
        hour: float, minute: float, second: float, day_night_division: DayNightDivision
    ) -> Time:
        """
        Преобразует углы часов, минут, секунд.

        :param hour: Часы.
        :param minute: Минуты.
        :param second: Секунды.
        :param day_night_division: Переменная, обозначающая текущее время суток.

        :return Преобразованные часы, минуты, секунды.
        """
        hour = (hour // TimeConsts.HOUR_TO_DEGREES) % TimeConsts.ANALOG_HOURS
        if (
            day_night_division == DayNightDivision.PM.value
            and hour != TimeConsts.MIDDLE_DAY
        ):
            hour += TimeConsts.ANALOG_HOURS
        elif (
            day_night_division == DayNightDivision.AM.value
            and hour == TimeConsts.MIDDLE_DAY
        ):
            hour = hour
        minute = minute // TimeConsts.MINUTE_TO_DEGREES
        second = second // TimeConsts.SECOND_TO_DEGREES
        return Time(int(hour), int(minute), int(second))
