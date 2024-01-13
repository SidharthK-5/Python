"""
Generate a dataframe from given numbers if the matrix order is satisfied
"""

import pandas as pd

rows, cols = map(int, input().split())
input_list = input().split()

if rows * cols == len(input_list):
    # Matrix order is statisfied
    data = dict()
    for i in range(rows):
        # Each row will have 'cols' no. of elements in it
        row = pd.Series(input_list[:cols])
        data[i] = row
        input_list = input_list[cols:]
    dataframe = pd.DataFrame(data).T
    print(dataframe)
else:
    print("Weird Order!")
