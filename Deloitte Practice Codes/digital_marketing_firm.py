"""
Enter the details of Entries and find the result based on average of 'open_rate'
"""

import pandas as pd

num_entities = int(input())
campaign_name = input().split()
no_of_emails = list(map(int, input().split()))
open_rate = list(map(int, input().split()))

# Create dataframe from input details
details = {
    "campaign_name": campaign_name,
    "no_of_emails": no_of_emails,
    "open_rate": open_rate,
}
dataframe = pd.DataFrame(details)
mean_of_opening = dataframe[
    "open_rate"
].mean()  # Find the mean of 'open_rate' values column

for value in dataframe["open_rate"]:
    if value >= mean_of_opening:
        print(True)
    else:
        print(False)
