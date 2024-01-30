"""
Using lambda functions within map()
"""

# map()
sample_list = [10, 20, 30, 40, 50]
print(f"{sample_list=}")

# This lambda calculates square of every element from 'sample_list'
sample_list_sqaured = list(map(lambda number: number**2, sample_list))
print(f"\n{sample_list_sqaured=}")

# number_1 is taken from sample_list, number_2 is taken from sample_list_sqaured
summed_list = list(
    map(
        lambda number_1, number_2: number_1 + number_2, sample_list, sample_list_sqaured
    )
)
print(f"\nList of sum of elements from above two lists: {summed_list}")

# filter()
# Filters the values from 'sample_list', which satisfies the given lambda (multiples of 20)
multiples_of_twenty = list(filter(lambda number: number % 20 == 0, sample_list))
print(f"\nMultiples of 20 from sample_list: {multiples_of_twenty}")

# Dict sorting based on values
sample_dict = {8: 50, 3: 40, 2: 30, 1: 20, 5: 10}
print(f"\n{sample_dict=}")

# key will take the lambda fn and lambda inputs a tuple (sample_dict.items()) and returns tupl[1] or value in tuple.
# This key is used by sorted() function
sample_dict_sorted = dict(sorted(sample_dict.items(), key=lambda tupl: tupl[1]))
print(f"\nsample_dict sorted based on values: {sample_dict_sorted}")
