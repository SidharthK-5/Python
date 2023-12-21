def WordCount(s):
    #your code here
    d = {}
    s = s.split()
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    #return dictionary object
    return d

#read a string S
S = input()
#Call the function
D = WordCount(S)
#Display the dictionary object
print(D)