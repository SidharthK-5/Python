"""
WIP: detect_html_tags.py
"""

import re

pattern = r'<(\w+)(.*?)>'
N = int(input())
html = "".join(input() for _ in range(N))
matches = re.findall(r'<!--.*?-->|<(\w+)(.*?)>', html, re.DOTALL)

for match in matches:
    tag = match[0]
    attributes = match[1]
    if tag:
        print(tag)
    if attributes:
        individual_attributes = attributes.split()
        for attribute in individual_attributes:
            print(f"{attribute=}")
            try:
                key, value = attribute.split('=')
                print("-> " + key + " > " + value.strip('"').strip("'").strip("/").strip('"').strip("'"))
            except ValueError:
                pass