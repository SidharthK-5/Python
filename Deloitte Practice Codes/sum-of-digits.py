def SumOfDigits(n):
    #write the function body here
    n = str(n)
    l = list(map(int, n))
    print(sum(l))
    
    
#call the function here
n = int(input())
SumOfDigits(n)