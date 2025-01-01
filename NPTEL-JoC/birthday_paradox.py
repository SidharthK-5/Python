"""
Birthday Paradox - Find your twin
The program generates a list of day-of-year of 50 people (50 numbers)
From the list, matching day-of-year are declared as twins
"""

import datetime
import random

birthdays = []
index = 0
start_year = 1900  # Assume the oldest person alive is born in 1900
current_year = int(datetime.date.today().strftime("%Y"))

while index < 50:
    # Set a random year
    year = random.randint(start_year, current_year)
    # Check if the year is leap year or not
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    else:
        leap = False

    # Set a random month
    month = random.randint(1, 12)

    # Set a random day based on month value
    if month == 2 and leap:
        day = random.randint(1, 29)
    elif month == 2 and leap is False:
        day = random.randint(1, 28)
    elif month == 7 or month == 8:  # Handling July & August
        day = random.randint(1, 31)
    elif month % 2 != 0 and month < 7:
        day = random.randint(1, 31)
    elif month % 2 == 0 and month > 8 and month < 12:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    converted_date = datetime.date(year=year, month=month, day=day)
    day_of_year = converted_date.timetuple().tm_yday
    birthdays.append(day_of_year)
    index += 1
birthdays.sort()
print("The day of year of birthdays of 50 people are:")
print(f"{birthdays=}")

print("\nTwins are found for:")
for date in range(1, len(birthdays)):
    if birthdays[date] == birthdays[date - 1]:
        print(f"Twin found for {birthdays[date]}")
