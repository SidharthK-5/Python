"""
Given two lists. Merge them into a pandas dataframe
"""

import pandas as pd
import numpy as np

# start, end and step values of list1
start, end, step = map(int, input().split())
# The input values are directly converted to numpy array
list2 = np.array(list(input().split()))
# Column titles of list1 and list2
first, second = map(str, input().split())
# n => how many elements are needed, pos => from which end 'n' elements are needed
n, pos = map(int, input().split())

list1 = np.arange(start, end+1, step)
list1 = pd.Series(list1)
list2 = pd.Series(list2)

"""
Converting two Series into a DF
    1. The 2 Series must be passed within []
    2. Since we're not converting a dict into DF, key= must be given. Else it will be taken as 0,1,2....
    3. axis=1 means concat along columns, axis=0 means concat along indices
"""
dataframe = pd.concat([list1, list2], keys=[first, second], axis=1)

# If pos is zero, access elements from the end. Else from beginning
if pos == 0:
    print(dataframe.tail(n))
else:
    print(dataframe.head(n))