"""
Create a numpy array using the start, end and step value given
"""

import numpy as np

# Read the start, end and step value for array
start = int(input())
end = int(input())
step = int(input())

# Check for array feasibility
if (end-start)%step == 0 or start+step < end:
    #  Your logic for operations
    array = np.arange(start, end+1, step)
    for i in array:
        print(i)
else:
    print("Constraints are failing!")