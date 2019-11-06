import requests
import json

# apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://github.com/dewaledr/dataRepresentation'
filename = 'repoFA.json'

# response = requests.get(url, auth=('token', apiKey))
response = requests.get(url, params="")
repoJSON = response.json()
# print(response.status_code)
print("1...")
# print(response.content)
print("2...")


# read from a private repos with apiKey
file = open(filename,"w")
json.dump(repoJSON, file, indent=4)
print("4...")

# use curl  f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85
# curl -i -H " Authorization: token b4ddb9e5603da11cd857b83bad6ea6eb1819b92d" https://api.github.com/repos/datarepresentationstudent/aPrivateOne
# curl -i -H "Authorization: token f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85, Accept: application/vnd.github.v3+json" https://api.github.com/repos/datarepresentationstudent/aPrivateOne
# From my account
# curl -i -H "Accept: application/vnd.github.v3+json" https://github.com/dewaledr/dataRepresentation