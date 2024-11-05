from datetime import datetime

from clocks.digital_clock_adapter import DigitalClockAdapter
from clocks.analog_clock import AnalogClock

if __name__ == "__main__":
    analog_clock = AnalogClock()
    digital_clock_adapter = DigitalClockAdapter(analog_clock)

    date_time_input = datetime(2024, 11, 5, 12, 30)
    digital_clock_adapter.set_date_time(date_time_input)

    print("Время (цифровые часы):", digital_clock_adapter.get_date_time())
