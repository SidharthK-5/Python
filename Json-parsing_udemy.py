import json
from traceback import print_tb

handle = open("json_input.json", "r")
content = handle.read()
#print(content)
handle.close()

d = json.loads(content)
print(d['database']['port'])

d['database']['port'] = 3330
d['files']['log'] = ('/log/app.log','/log/mysql/app.log' )
print(d)

handle = open("json_output.json", "w")
j = json.dumps(d, indent=4, sort_keys=True)
handle.write(j)
