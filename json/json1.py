import json	

f = open("sample.json","r")
data = json.load(f)
print( json.dumps(data["st2"]["name"],indent=2) )
f.close()