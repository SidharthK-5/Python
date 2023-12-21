"""Generator fn are used if the fn creates a large series of nos. yield will stop the multiple times execution
exectues only once and wait for the next call of next(). This saves memory"""

# Fibonacci using generator
def fibo():
    first = 0
    yield first
    second = 1
    yield second
    while(True):
        next = first + second
        yield next
        first,second = second,next

g = fibo()    
for i in range(10):
    print(next(g))

# Generator concept in comprehension
l = [10,20,30,40,50]
l2 = (value**2 for value in l) # Giving () instead of [] will create a generator object l2
for i in range(len(l)):
    print(next(l2))
