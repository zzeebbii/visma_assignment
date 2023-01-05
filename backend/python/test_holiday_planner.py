import unittest
from datetime import date, timedelta
from holiday_planner import HolidayPlanner


class HolidayPlannerTests(unittest.TestCase):
    def test_count_days(self):
        start_date = date(year=2022, month=4, day=1)
        end_date = date(year=2022, month=4, day=30)
        day_counter = HolidayPlanner(start_date, end_date)
        num_days = day_counter.count_days()
        self.assertEqual(num_days, 24)

    def test_count_days_same_day(self):
        start_date = date(year=2022, month=4, day=1)
        end_date = date(year=2022, month=4, day=1)
        day_counter = HolidayPlanner(start_date, end_date)
        num_days = day_counter.count_days()
        self.assertEqual(num_days, 1)

    def test_count_days_different_month(self):
        start_date = date(year=2022, month=4, day=15)
        end_date = date(year=2022, month=5, day=31)
        day_counter = HolidayPlanner(start_date, end_date)
        num_days = day_counter.count_days()
        self.assertEqual(num_days, 37)

    def test_count_days_different_country(self):
        start_date = date(year=2022, month=4, day=15)
        end_date = date(year=2022, month=5, day=31)
        day_counter = HolidayPlanner(start_date, end_date)
        num_days = day_counter.count_days(country="Pakistan")
        self.assertEqual(num_days, 40)

    def test_invalid_range(self):
        start_date = date(year=2022, month=3, day=1)
        end_date = date(year=2022, month=4, day=1)
        day_counter = HolidayPlanner(start_date, end_date)
        with self.assertRaisesRegex(ValueError, "Range is not in the same holiday period"):
            day_counter.count_days()

    def test_invalid_start_date(self):
        start_date = date(year=2022, month=5, day=1)
        end_date = date(year=2022, month=4, day=30)
        day_counter = HolidayPlanner(start_date, end_date)
        with self.assertRaisesRegex(ValueError, "chronological"):
            day_counter.count_days()

    def test_invalid_range_length(self):
        start_date = date(year=2022, month=1, day=1)
        end_date = date(year=2022, month=3, day=1)
        day_counter = HolidayPlanner(start_date, end_date)
        with self.assertRaisesRegex(ValueError, "Range should not be more than 50"):
            day_counter.count_days()
