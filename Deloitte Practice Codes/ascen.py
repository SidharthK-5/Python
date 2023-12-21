def ascending(ls):
    print(ls)
    #your code here
    # while ls.count(',') > 0:
    #     ls.remove(',')
    # while ls.count(' ') > 0:
    #     ls.remove(' ')
    
    if len(ls) < 2:
        ret = True
    else:
        ret = False
    
    flag = 0
    for i in range(len(ls)-1):
        if int(ls[i]) > int(ls[i+1]):
            flag = 1
            break
    if flag == 0:
        ret = True
    else:
        ret = False
    #return true or False
    return ret

#read the data elements for list
l = input().split(', ')
#call the function
ret = ascending(l)
#display the result
print(ret)

def ascending(ls):
    n=len(ls)
    i=1
    k=0
    if n==0:
        return True
    else:
        while(i<n):
            if (ls[i]<ls[i-1]):
                k=k+1
            i=i+1
        if k==0:
            return True
        else:
            return False


lst = list(map(int, input().split(',')))

val = ascending(lst)
print(val)