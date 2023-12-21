def get_list_item(lis, index):
    try:
        return lis[index]
    except IndexError:
        return None

my_list = [1,2,3,4,5,6,7]
print(get_list_item(my_list,8))

def w4(x, y=3):

    if y < 0:
        raise ValueError("y must be greater than 0")
    
    z = x*y
    w = z + '!!'
    return w

print(w4("Yay", 5))