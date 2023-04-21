import calendar
from typing import Optional


class HolidaysCalendar:
    def __init__(self, list_of_the_week_holidays: list[Optional[int]] = []):
        self.holidays_days = list_of_the_week_holidays

    def is_holiday(self, a_potential_holiday: int) -> bool:
        return self.is_weekday_holiday(a_potential_holiday)

    def is_weekday_holiday(self, a_potential_holiday: int)-> bool:
        return a_potential_holiday in self.holidays_days