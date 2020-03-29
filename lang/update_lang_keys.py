import json
import os
str = input("Lang file: ")
lang = dict()
if os.path.isfile(str+".json"):
        langFile = open(str+".json", "r", encoding="utf-8")
        lang = json.load(langFile)
        try:
        	lang = json.load(langFile)
        except json.JSONDecodeError:
        	pass
        langFile.close()
materialsFile = open("materials.txt", "r", encoding="utf-8")
for material in materialsFile:
	if material.strip():
		key = "jaopca.material."+material.strip()
		if key not in lang:
			lang[key] = ""
langFile = open(str+".json", "w", encoding="utf-8")
json.dump(lang, langFile, sort_keys=True, indent=4)
langFile.close()
