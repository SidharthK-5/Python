"""
Given an HTML code snippet of N lines.
Task is to detect and print all the HTML tags, attributes and attribute values.
"""

from html.parser import HTMLParser


class HTMLTagParser(HTMLParser):
    def handle_starttag(self, tag, att):
        print(tag)
        self.print_atributes(att)

    def print_atributes(self, att):
        for name, val in att:
            print(f"-> {name} > {val}")


parser = HTMLTagParser()
for _ in range(int(input())):
    parser.feed(input())
