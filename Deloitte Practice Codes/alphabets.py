"""
Print index number and corresponding english alphabet
Take a string input and create a Pandas Series in that name
"""

import pandas as pd

alphabets = "abcedfghijklmnopqrstuvwxyz"
alphabets_list = list(alphabets)

# Input series name from STDIN
series_name = input()
series = pd.Series(list(series_name))
name = series.rename(series_name)

# Print output to STDOUT
for idx in range(10):
    print(idx, alphabets_list[idx], sep="     ")
for idx in range(10, 26):
    print(idx, alphabets_list[idx], sep="    ")

print(f"Name: {series_name}, dtype: {series.dtype}")
