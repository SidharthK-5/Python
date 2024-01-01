"""
Enter the side lengths of a triangle in the descending order
to check if it is right angled or not
"""

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if not(a>b and b>c):
        print('INVALID_INPUT')
    elif b**2 + c**2 == a**2:
        print('RIGHT ANGLE TRIANGLE')
    else:
        print('NOT RIGHT ANGLE TRIANGLE')
    
main()