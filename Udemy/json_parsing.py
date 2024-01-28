"""
Reading and Writing JSON using python
"""

import json

handle = open("data/json_input.json", "r")
content = handle.read()
print(f"JSON content: \n{content}\n")
handle.close()

dictionary = json.loads(content)
print(f"""{dictionary["database"]["port"]=}""")

dictionary["database"]["port"] = 3330
dictionary["files"]["log"] = ("/log/app.log", "/log/mysql/app.log")
print(f"{dictionary=}")

handle = open("data/json_output.json", "w")
json_sample = json.dumps(dictionary, indent=4, sort_keys=True)
handle.write(json_sample)
