import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"
response = requests.get(url)
data = response.json()
###Print to console
#print(response.headers)
# print(data)

# for car in data["cars"]:
#     print(car)

### Write to file
# filename = 'cars.json'
# if filename:
#     #Write json data
#     with open(filename,'w') as f:
#         json.dump(data, f, indent=4)

### Write to excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0
ws.write(row,0,"Reg")
ws.write(row,1,"Make")
ws.write(row,2,"Model")
ws.write(row,3,"Price")
row += 1
for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row += 1
w.save('cars.xls')
