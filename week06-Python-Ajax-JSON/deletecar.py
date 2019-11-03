# Write a python program that deletes a car on the server by using the API
import requests

carString = {'reg':'08 C 1234', 'make':'Ford', 'model':'Galaxy', 'price':2500}
url = 'http://127.0.0.1:5000/cars/08%20C%201234'
response = requests.delete(url)
print("...header..")
print(response.headers)
print("..code...")
print(response.status_code)
print("..text...")
print(response.text)
