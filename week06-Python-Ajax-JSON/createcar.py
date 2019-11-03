# Write a python program that creates a car on the server by using the API
import requests
import json

carString = {'reg':'08 C 1234', 'make':'Ford', 'model':'Galaxy', 'price':2500}
url = 'http://127.0.0.1:5000/cars'
response = requests.post(url, json=carString)
print("...header..")
print(response.headers)
print("..code...")
print(response.status_code)
print("..text...")
print(response.text)

