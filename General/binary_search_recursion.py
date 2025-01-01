"""
Program to perform binary serach using recursion
"""


def binary_search(array, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return binary_search(array, low, mid - 1, key)
        else:
            return binary_search(array, mid + 1, high, key)
    else:
        return -1


if __name__ == "__main__":
    array = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the target element: "))
    array = sorted(array)
    result = binary_search(array, 0, len(array) - 1, target)
    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found")
