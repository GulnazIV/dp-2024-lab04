import unittest
from datetime import datetime

from clocks.digital_clock_adapter import DigitalClockAdapter
from clocks.analog_clock import AnalogClock


class TestAnalogToDigitalClockAdapter(unittest.TestCase):

    def setUp(self):
        """
        Устанавливает начальные условия для тестов, создавая экземпляр
        аналоговых часов и адаптера.
        """
        self.analog_clock = AnalogClock()
        self.adapter = DigitalClockAdapter(self.analog_clock)

    def test_set_and_get_date_time(self):
        """
        Тестирует, что установленные значения совпадают с полученными.
        """
        test_datetime = datetime(2024, 11, 5, 15, 30)

        self.adapter.set_date_time(test_datetime)
        result_datetime = self.adapter.get_date_time()

        self.assertEqual(result_datetime.year, test_datetime.year)
        self.assertEqual(result_datetime.month, test_datetime.month)
        self.assertEqual(result_datetime.day, test_datetime.day)
        self.assertEqual(result_datetime.hour, test_datetime.hour)
        self.assertEqual(result_datetime.minute, test_datetime.minute)
        self.assertEqual(result_datetime.second, test_datetime.second)

    def test_day_night_division(self):
        """
        Тестирует правильность установки AM/PM в зависимости от времени.
        """
        day_time = datetime(2024, 11, 5, 0, 30, 15)
        night_time = datetime(2024, 11, 5, 12, 30, 15)

        self.adapter.set_date_time(day_time)
        result_day = self.adapter.get_date_time()

        self.adapter.set_date_time(night_time)
        result_night = self.adapter.get_date_time()

        self.assertEqual(result_day.hour, 0)
        self.assertEqual(result_night.hour, 12)


if __name__ == "__main__":
    unittest.main()
