# fizzbuzz
n = int(input())
for num in range(1,n+1):
    if num % 15 == 0:
        print("fizzbuzz")
    else:
        if num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
            
