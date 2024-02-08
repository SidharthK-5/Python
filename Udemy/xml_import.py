"""
Reading and parsing XML files
"""

import xmltodict

handle = open("data/xml_input.xml", "r")

xml_content = handle.read()
print(f"{xml_content=}")

dict_of_xml = xmltodict.parse(xml_content)
print(f"\n{dict_of_xml=}")

dict_of_xml["Result"]["Requestcode"] = 4
print(f"After changing, {dict_of_xml=}")

dict_to_xml = xmltodict.unparse(dict_of_xml)
print(f"\n{dict_to_xml=}")
