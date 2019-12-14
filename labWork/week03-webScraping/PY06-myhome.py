import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

#soup = BeautifulSoup(page.content, 'html.parser')

soup = BeautifulSoup(page.content, 'html.parser')
# listings = soup.find("div", class_="PropertyListingCard")
listings = soup.findAll("div", class_="PropertyListingCard")
for listing in listings:
    entry = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entry.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entry.append(address)
    print(entry)
#print(address)
