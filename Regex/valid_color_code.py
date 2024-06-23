"""
Program to extract valid color codes from a given CSS code.
Occurences of CSS selectors should be ignored.
"""

import re

color_pattern = r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}"

N = int(input())
valid_colors = []
selector_flag = False
code_lines = [input() for _ in range(N)]
for line in code_lines:
    if "{" in line:
        selector_flag = True
        continue
    elif "}" in line:
        selector_flag = False
    if selector_flag:
        valid_colors.extend(re.findall(pattern=color_pattern, string=line))

print(*valid_colors, sep="\n")
