def intreverse(n):
    #your code here
    if n>0:
        ret = int(str(n)[::-1])
    else:
        ret = "Invalid Input"
    
    #return the reversed number
    return ret
    

#read a number
n = int(input())
# call the function and display the result
print(intreverse(n))