import hashlib
import time
import json
#---------------------------------
STORAGE_FOLDER = "../../storage/fragments/"
LINK = "http://127.0.0.1:4040/flow/"
#---------------------------------
def flowPost(json):
	fragment = createFragment(json)
	store(fragment)
	
	return LINK+fragment["hash"]

def createFragment(json):
	fragment = {}
	fragment["time"] = time.ctime(time.time())
	fragment["who"] = json["who"]
	fragment["content"] = json["content"]
	key = fragment["who"] + fragment["time"]
	fragment["hash"] = hashlib.sha224(bytes(key, "utf-8")).hexdigest()

	return fragment

def store(fragment):
	with open(STORAGE_FOLDER+fragment["hash"]+".json", "w") as f:
		f.write(json.dumps(fragment))
	print("stored: " + fragment["hash"])
#---------------------------------
"""
import json

#JSON to DICT
dict = json.load(json_file)

#DICT to JSON
json_file = json.dumps(dict)
"""