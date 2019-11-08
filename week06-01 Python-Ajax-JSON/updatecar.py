# Write a python program that updates a car on the server by using the API
import requests
import json

carString = {'make':'Ford', 'model':'KUGA'}
url = 'http://127.0.0.1:5000/cars/test'
response = requests.put(url, json=carString)
print("...header..")
print(response.headers)
print("..code...")
print(response.status_code)
print("..text...")
print(response.text)
