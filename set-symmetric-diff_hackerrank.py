n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

print(len(english_set.symmetric_difference(french_set)))
