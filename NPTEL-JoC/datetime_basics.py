"""
Basics of datetime module
"""


import datetime


print("Basics of datetime module")
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().strftime('%Y')}")
print(f"Current month: {datetime.date.today().strftime('%B')}")
print(f"Current date: {datetime.date.today().strftime('%d')}")
print(f"Week number of this year: {datetime.date.today().strftime('%W')}")
print(f"Weekday of the week: {datetime.date.today().strftime('%w')}")
print(f"Day of the year: {datetime.date.today().strftime('%j')}")
print(f"Day of week: {datetime.date.today().strftime('%A')}")
print(f"Date and Time: {datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}")
