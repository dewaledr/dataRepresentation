# Read all users following Andrew Beatty from github
# Write to Spreadsheet loginID and repos address
import requests, json
from xlwt import *

#carString = {'reg':'08 C 1234', 'make':'Ford', 'model':'Galaxy', 'price':2500}
url = 'https://api.github.com/users/andrewbeattycourseware/followers'
response = requests.get(url)
data = response.json()

# # messy output
# print(data)

# # Get the file name for the new file to write to
# filename = 'githubusers.json'
# with open(filename, 'w') as  f:
#     json.dump(data, f, indent=4)

# Write it to Excel
w = Workbook()
ws = w.add_sheet('andyFollow')
row = 0
ws.write(row,0,"Users Login")
ws.write(row,1,"Users ID")
ws.write(row,2,"Repos URL")
row += 1
for name in data[:]:
    ws.write(row, 0, name["login"])
    ws.write(row, 1, name["id"])
    ws.write(row, 2, name["repos_url"])
    row += 1
w.save('andrewFollowers.xls')
