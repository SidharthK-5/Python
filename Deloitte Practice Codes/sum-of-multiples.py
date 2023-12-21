def SumOfMultiples(n):
    #your code here
    s = 0
    for i in range(n+1):
        if i%3 == 0 or i%5 == 0:
            s += i
        
    #return the value of sum
    return s
  
#Read the value of limit
n = int(input())
#call the function
summed_value = SumOfMultiples(n)
# display sum of multiples of 3 and 5 within the given limit
print(summed_value)