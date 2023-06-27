import json
import sys

import json
data={}
with open('json.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
if (sys.argv[1]=='n'):
	print(len(data["nodes"]))
	data["nodes"].append({"id":len(data["nodes"]),"label":sys.argv[2],"link":sys.argv[3]})
if (sys.argv[1]=='l'):
	data["links"].append({"source":int(sys.argv[2]),"target":int(sys.argv[3])})
if (sys.argv[1]=='a'): #new author
	data["authors"].append({"id":len(data["authors"]),"name":sys.argv[2],"link":sys.argv[3]})
if (sys.argv[1]=='aa'): #add author 2 to node 3
	data["nodes"][int(sys.argv[3])]["author"]=int(sys.argv[2])

with open('json.json', 'w', encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)
