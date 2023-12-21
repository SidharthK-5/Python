n = int(input())
eng_list = set(map(int, input().split()))
b = int(input())
french_list = set(map(int, input().split()))

print(len(eng_list.intersection(french_list)))