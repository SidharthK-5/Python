"""
Find the LCM of number pairs
"""


def find_lcm(pair: list[int]) -> int:
    """
    Find the LCM of number pair

    Args:
        pair (list[int]): list of numbers to find LCM

    Returns:
        int: LCM of two numbers
    """
    num_1, num_2 = map(int, pair)
    if num_1 < 1 or num_1 > 1000 or num_2 < 1 or num_2 > 1000:
        return "Out of Range!"
    elif num_1 == 1 or num_2 == 1:
        return max(num_1, num_2)
    else:
        # Create sets of multiples of the numbers
        s1 = set(range(num_1, num_1 * num_2 + 1, num_1))
        s2 = set(range(num_2, num_1 * num_2 + 1, num_2))

        # Create a set of common multiples of these numbers
        s3 = s1.intersection(s2)
        return min(s3)


num_of_pairs = int(input())
list_of_pairs = []
for _ in range(num_of_pairs):
    list_of_pairs.append(input().split())

for num_pair in list_of_pairs:
    lcm = find_lcm(num_pair)
    print(lcm)
