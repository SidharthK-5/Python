import xmltodict

handle = open("xml_input.xml", "r")

content = handle.read()
# print(content)
d = xmltodict.parse(content)
print(d)

d["Result"]["Requestcode"] = 4

x = xmltodict.unparse(d)
print(x)
