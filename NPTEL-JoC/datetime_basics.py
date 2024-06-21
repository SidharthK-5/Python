"""
Basics of datetime module
"""


import datetime


print("\nBasics of datetime module\n")
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().strftime('%Y')}")
print(
    f"Current year without century as decimal number: {datetime.date.today().strftime('%y')}"
)
print(f"Current month: {datetime.date.today().strftime('%B')}")
print(f"Current date: {datetime.date.today().strftime('%d')}")
print(
    f"Week number of this year (Sun as 1st day of the week): {datetime.date.today().strftime('%U')}"
)
print(
    f"Week number of this year (Mon as 1st day of the week): {datetime.date.today().strftime('%W')}"
)
print(f"Weekday of the week: {datetime.date.today().strftime('%w')}")
print(f"Day of the year: {datetime.date.today().strftime('%j')}")
print(f"Day of week: {datetime.date.today().strftime('%A')}")
print(f"Day of week shortened: {datetime.date.today().strftime('%a')}")
print(
    f"Date and Time (24 hr): {datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"
)
print(
    f"Date and Time (12 hr): {datetime.datetime.now().strftime('%d/%m/%Y, %I:%M:%S %p')}"
)
print(
    f"Locale's appropriate date and time rep: {datetime.datetime.now().strftime('%c')}"
)
print(f"Locale's appropriate date rep: {datetime.datetime.now().strftime('%x')}")
print(f"Locale's appropriate time rep: {datetime.datetime.now().strftime('%X')}")
