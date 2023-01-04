from datetime import date, timedelta


class HolidayPlanner:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.holidays = {
            "Finland": [
                date(2021, 1, 1),
                date(2021, 1, 6),
                date(2021, 4, 2),
                date(2021, 4, 5),
                date(2021, 5, 13),
                date(2021, 6, 25),
                date(2021, 12, 6),
                date(2021, 12, 24),
                date(2022, 1, 1),
                date(2022, 1, 6),
                date(2022, 4, 15),
                date(2022, 4, 18),
                date(2022, 5, 1),
                date(2022, 5, 26),
                date(2022, 6, 5),
                date(2022, 6, 24),
                date(2022, 6, 25),
                date(2022, 12, 6),
                date(2022, 12, 24),
                date(2022, 12, 25),
                date(2022, 12, 26),
            ]
        }

    def is_range_valid(self):
        # Ensure that start_date is not after end_date
        if self.start_date > self.end_date:
            raise ValueError("Input dates should be in chronological order")

        # Ensure that the difference between start_date and end_date is not more than 50 days
        diff = self.end_date - self.start_date
        if diff.days > 50:
            raise ValueError("Range should not be more than 50")

        if self.start_date.month < 4 and self.end_date.month > 3:
            raise ValueError("Range is not in the same holiday period")

        return True

    def count_days(self, country="Finland"):
        if self.is_range_valid():
            # Get the list of holidays for the given country
            country_holidays = self.holidays.get(country, [])

            # Initialize a counter for the number of days
            num_days = 0

            # Create a new date object set to the start date
            current_date = self.start_date

            # Iterate over the date range
            while current_date <= self.end_date:
                # Check if the day is a Sunday or a holiday
                if current_date.weekday() != 6 and current_date not in country_holidays:
                    num_days += 1

                current_date += timedelta(days=1)

            return num_days
