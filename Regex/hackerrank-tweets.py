"""
Program to detect no. of tweets containing the word 'hackerrank'
"""

import re


N = int(input())
tweets = [input() for _ in range(N)]
pattern = re.compile(r"\bhackerrank\b", re.IGNORECASE)

count = 0
for tweet in tweets:
    if pattern.search(tweet):
        count += 1

print(count)
