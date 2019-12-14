import requests
import json

dt = {
    'name':'joe',
    'age': 22,
    'Student?': True
}
print(dt)

# Put in a file
file = open("simplePrinted.json",'w')
json.dump(dt, file)

# Put in a file, make it look neater with indent
file = open("simplePrinted4.json",'w')
json.dump(dt, file, indent=4)

# Just convert to string and maybe, pass to a server. Lets's print it.
jsonString = json.dumps(dt)
print(jsonString)


