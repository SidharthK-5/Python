def AlphabetCount(s):
    #your code here
    d = {}
    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    #return dictionary object
    return d

#read the string S
S = input()
#Call the function
D = AlphabetCount(S)
#Display the dictionary
print(D)