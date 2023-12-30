"""
Sample statistics tools and plotting utils in python
"""

import statistics
import matplotlib.pyplot as plt
import random


def make_random_list(min: int, max: int, num_elements: int) -> list[int]:
    """
    Creates a list of 'num_elements' random number within the range [min, max]
    Args:
        min (int): minimum value in the random list
        max (int): maximum value in the random list
        num_elements (int): no. of elements needed in the list

    Returns:
        list[int]: a list of random numbers
    """
    random_list = []
    for i in range(num_elements):
        random_list.append(random.randint(min, max))
    
    return random_list


estimates = [350, 355, 360, 365, 380, 385, 390, 395, 398, 400]
results = make_random_list(1,10,10)

plt.plot(estimates, results, 'r--')
plt.plot([statistics.mean(estimates)], [5], 'go') # Green circle label for mean
plt.plot([statistics.median(estimates)], [5], 'bs') # Blue sqaure label for mean
# Setting plot title and labels
plt.title(label="Statistical Plot")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.show()