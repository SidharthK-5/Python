"""
Creating a Hackerrank logo using character 'H'
Replaced all ______ with rjust, ljust or center suitably. 
"""

thickness = int(input())  # This must be an odd number
c = "H"

# Top Cone
for i in range(thickness):
    # left 'H' ladder with .rjust + 'H' + right ladder with .ljust
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # 1st pillar is centered with thickness*2 spaces + 2nd pillar is centered with thickness*6 times spaces
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Belt height is CEIL(thickness/2). Belt width is 5*thickness and is centered with 6*thickness
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # 1st pillar is centered with thickness*2 spaces + 2nd pillar is centered with thickness*6 times spaces
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # right 'H' ladder with .rjust + 'H' + left 'H' ladder with .ljust. The whole bottom cone is .rjust with 6*thickness to push towards right pillar
    print(
        (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )
