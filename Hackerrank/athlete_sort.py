"""
Question: Sort a 2D list based on k'th index of the sub lists
In the final result, the sub lists will be sorted in the outer list based on k'th index position of sub lists
"""

from operator import itemgetter

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # Sort using key as k. itemgetter grabs the k'th index of sub lists and pass it as the sort key
    for row in sorted(arr, key=itemgetter(k)):
        print(*row)