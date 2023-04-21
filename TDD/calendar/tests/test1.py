import unittest
import calendar

from TDD.calendar.domain.holidays_calendar import HolidaysCalendar


class DaysOfTheWeekAreHolidays(unittest.TestCase):

    def test_a_day_of_the_week_can_be_holiday(self):
        # Setup
        a_day_of_the_week = calendar.SUNDAY
        holidays_calendar = HolidaysCalendar()
        holidays_calendar.mark_days_as_holidays.append(a_day_of_the_week)
        # Exercise
        result = holidays_calendar.is_holiday(a_day_of_the_week)
        # Verify
        self.assertEqual(result, True)

    def test_a_day_of_the_week_is_can_not_be_holiday(self):
        # Setup
        day_of_the_week = calendar.MONDAY
        holidays_calendar = HolidaysCalendar()
        # Exercise
        result = holidays_calendar.is_holiday(day_of_the_week)
        # Verify
        self.assertEqual(result, False)

    def test_several_days_of_the_week_can_be_holiday(self):
        # Setup
        a_day_of_the_week = calendar.SATURDAY
        another_day_of_the_week = calendar.SUNDAY
        holidays_calendar = HolidaysCalendar()
        holidays_calendar.mark_days_as_holidays = [a_day_of_the_week, another_day_of_the_week]
        # Exercise
        result_1 = holidays_calendar.is_holiday(a_day_of_the_week)
        resull_2 = holidays_calendar.is_holiday(another_day_of_the_week)
        # Verify
        self.assertEqual(result_1, True)
        self.assertEqual(resull_2, True)



if __name__ == '__main__':
    unittest.main()
