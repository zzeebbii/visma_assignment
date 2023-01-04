from datetime import date
from holiday_planner import HolidayPlanner

start_date = date(2022, 4, 1)
end_date = date(2022, 4, 30)

day_counter = HolidayPlanner(start_date, end_date)
num_days = day_counter.count_days()

print(num_days)
