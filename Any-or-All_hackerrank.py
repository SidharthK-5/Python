""" Question: Using any() and all() methods:
                Print True if all elements of a list are positive and then if any one of them is palindrome
                Else, print False
    The code should be 3 lines max"""

N = int(input())
l = list(map(str, input().split()))
# The inner all will check if all elements are +ve and any will check if atleast one is palindrome.
# These two results are treated as elemtents for the outer all(), so as to combine the decision
print(all([all(i>'0' for i in l), any(i == i[::-1] for i in l)]))