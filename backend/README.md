# HolidayPlanner Class

## Problem statement

The problem statement is itself easy to understand. We have two dates as input and we can call them `start_date` and `end_date`. We want to calculate the number of days between these two dates with certain exceptions which are:

- Sunday should not be included in the counting
- Days from a list should also be excluded from the counting if they fall between the range

Other than these exceptions, we have some validation requirements which are:

- `start_date` should not be before `end_date` (Chronological)
- Total number of days for the range should not be more than **50**. I am assuming that this includes the whole week and no exceptions.

## Challenges

First of all, we know that it is going to be a `class` so we can take the `start_date` and `end_date` as input (in constructor) when the user will initialize the object. These two variables will be stored as class variables. The type of these two inputs can be either `string` or `Date` and for this assignment, we will take them as `Date` to keep things simple. It also makes sense to have them as type `Date` instead of `string` (personal opinion, one can argue).

After we have received the inputs then the next thing is to decide the validation. I won't do it during the initialization since it is not a good practice to throw exceptions from constructor. We will do the validation when the user will actually run the method `count_days` for the class.

We will create a private method in class called `validate_range` and its pseudo code is as follows:

```
    if start_date < end_date
        throw Error("Dates should be in chronological order")
    if end_date - start_date > 50
        throw Error("Range should not exceed 50 days")
    if start_date and end_date are not between 1st of April and 31st of March
        # This will require some work to figure out a logic.
        throw Error("Invalid period")

    # if all the checks are passing
    return true

```

Once we have initialization and `validate_range` are in place then we will proceed to the actual method, `count_days` which will count the days between these two dates. pseudo code is as follows:

```
    if validate_range() == True
        # this code will only be executed when the range is valid, otherwise exception will be thrown

        count = 0
        current_date = start_date

        while (current_date <= end_date)
            if current_date.day != Sunday
                count = count + 1

            current_date = current_date + 1 day

        return count
```

This logic is first implementation where we are excluding Sunday from the calculation. But the requirement also says that we should exclude public holidays and those should be specific to the country as well. Hmmm!

### Public holidays

If we were doing it for Finland only then it'd be easy to create a list of `exclusion_days` with all the public holidays in the list and then we could simply skip the day from count if it was in the list.

But we want it more generic and support all the countries. So, for that, we will define a class variable called `public_holidays` and it will be a dictionary/map where the keys will be the name of the country and the values will be the list containing all public holidays. For this implementation, we will simply hardcode the values, but in real world, the values can be read from some database/file.

Once the list is defined then either the user can specify the country on time of object creation with the two dates and we can store it in class variable or the user can specify it as an argument to `count_days`. Both have their benefits, for example:

- If we pass it in constructor and then store it in class variable then the user can name their objects like "finnish_holiday_planner" and "us_holiday_planner".
- The value will be passed in the constructor once and can be used later from the class variable

On the other hand, if we pass it directly to the `count_days`, then:

- We don't need to create an extra class variable
- One method `count_days` can produce different output based on the `country` passed as an argument

I'll go with the second approach for now.

**NOTE:** If the public holidays for the country are not available then we'll use an empty list
