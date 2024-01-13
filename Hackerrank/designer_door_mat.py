"""
Question: Create a desginer mat with the following criteria
1. Mat size must be N * M. (N is an odd natural number, and M is 3 times N.)
2. The design should have 'WELCOME' written in the center.
3. The design pattern should only use |, . and - characters.

Sample Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
"""

# Read N and M
N, M = map(int, input().split())

# Print the top section
for design_thickness in range(1, N, 2):
    print((".|." * design_thickness).center(M, "-"))

# Print the middle part
print("WELCOME".center(M, "-"))

# Print the bottom section
for design_thickness in range(N - 2, 0, -2):
    print((".|." * design_thickness).center(M, "-"))
