import requests
import json

apiKey = 'da42a72bfa816f16ea6df0a84e5dcb9646073f48'
# works url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
# works url = 'https://api.github.com/user/repos'
url = 'https://api.github.com/repos/dewaledr/aPrivateOne'
filename = 'repo.json'

response = requests.get(url, auth=('token', apiKey))
repoJSON = response.json()
print(response.status_code)  
# print(response.content)
#print(repoJSON)


# # read from above private repos with apiKey and write to a file
file = open(filename,"w")
json.dump(repoJSON, file, indent=4)

###
# works curl -i -H 'Authorization: token da42a72bfa816f16ea6df0a84e5dcb9646073f48' https://api.github.com/repos/dewaledr/aPrivateOne
#
# From my account
# curl -i -H "Accept: application/vnd.github.v3+json" https://github.com/dewaledr/dataRepresentation

# curl -i -H 'Authorization: token b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e' https://api.github.com/repos/datarepresentationstudent/aPrivateOne
# curl -i -H "Authorization: token f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85, Accept: application/vnd.github.v3+json" https://api.github.com/repos/datarepresentationstudent/aPrivateOne


