def ascending(ls):
    #your code here
    if ls == sorted(ls):
        ret = True
    else:
        ret = False
    #return true or False
    return ret

#read the data elements for list
l = list(map(int, input().split(',')))
#call the function
ret = ascending(l)
#display the result
print(ret)