def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num>0 and num<1000:
        bin = []
        while num>0:
            bin.append(str(num%2))
            num = num // 2
        print(''.join(bin)[::-1])
    else:
        print('INVALID_INPUT')

n = int(input())        
decimalToBinary(n)