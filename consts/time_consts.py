class TimeConsts:
    """
    Класс, содержащий константы, используемые для преобразования времени в углы для аналоговых часов.

    Атрибуты:
        HOUR_TO_DEGREES (int): Количество градусов, соответствующее одному часу (360° / 12 часов).
        MINUTE_TO_DEGREES (int): Количество градусов, соответствующее одной минуте (360° / 60 минут).
        SECOND_TO_DEGREES (int): Количество градусов, соответствующее одной секунде (360° / 60 секунд).
        ANALOG_HOURS (int): Общее количество часов на аналоговых часах.
        ANALOG_MINUTES (int): Общее количество минут в одном часе.
        MIDDLE_DAY (int): Обозначения полудня.
        MIDDLE_NIGHT (int): Обозначения полуночи.
    """

    HOUR_TO_DEGREES = 30
    MINUTE_TO_DEGREES = 6
    SECOND_TO_DEGREES = 6
    ANALOG_HOURS = 12
    ANALOG_MINUTES = 60
    MIDDLE_DAY = 12
    MIDDLE_NIGHT = 0
