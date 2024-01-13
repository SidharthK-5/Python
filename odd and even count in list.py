numbers = input().split()
odd_sum = 0
even_sum = 0
for value in numbers:
    if int(value) % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1

print("Number of even numbers :", even_sum)
print("Number of odd numbers :", odd_sum)
