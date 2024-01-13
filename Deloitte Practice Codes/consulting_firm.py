"""
Enter the details of Entries and find the result based on average of 'Marks'
"""

import pandas as pd

num_entities = int(input())
details = dict()
for entity in range(num_entities):
    details[entity] = input().split()

# Create dataframe from input details
dataframe = pd.DataFrame(details, index=["Name", "Age", "Marks", "Country"]).T
dataframe["Marks"] = dataframe["Marks"].astype(
    int
)  # Convert 'Marks' column to int type

# Calculate Result based on mean 'Marks' and add the column to dataframe
Result = [1.0 if i <= dataframe["Marks"].mean() else 0.0 for i in dataframe["Marks"]]
dataframe["Result"] = Result

# Output the variable to STDOUT
for entity in dataframe["Result"]:
    print(entity)
