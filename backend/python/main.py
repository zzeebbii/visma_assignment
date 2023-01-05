from datetime import date
from holiday_planner import HolidayPlanner

start_date = date(2022, 4, 15)
end_date = date(2022, 5, 31)

day_counter = HolidayPlanner(start_date, end_date)
num_days_finland = day_counter.count_days()

print(num_days_finland)

num_days_pakistan = day_counter.count_days(country="Pakistan")

print(num_days_pakistan)
