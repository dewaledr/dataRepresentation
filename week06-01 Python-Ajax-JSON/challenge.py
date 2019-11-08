# Read all users following Andrew Beatty from github
# Write a python program that creates a car on the server by using the API
import requests, json

#carString = {'reg':'08 C 1234', 'make':'Ford', 'model':'Galaxy', 'price':2500}
url = 'https://api.github.com/users/andrewbeattycourseware/followers'
response = requests.get(url)
data = response.json()

# messy output
print(data)

# Get the file name for the new file to write to
filename = 'githubusers.json'
with open(filename, 'w') as  f:
    json.dump(data, f, indent=4)

# Write it to Excel
