"""
Use calendar module to print the day of the week on a given date.
"""

import calendar


date, month, year = map(int, input().split())
"""
calendar.weekday will return the day_of_week as an integer
calendar.day_name will return the name of the day_of_week as a list
"""
print(calendar.day_name[calendar.weekday(year, date, month)].upper())
