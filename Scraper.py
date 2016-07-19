import sys
from bs4 import BeautifulSoup
import urllib.request
import os, csv, json

url = 'http://www.mysupermarket.co.uk/shelf/top_offers_from_across_the_uk'
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser') # Get the soup

items = soup.find_all('li', id='NgMspProductCell') # Find all listed items on page
names = soup.select('div[class=DetailsWrp] h3 a span') # Traverse the elements in the listed items
prices = soup.select('div[class=DetailsWrp] div[id=NgMspProductCellPrice] span[class=Price]')


basket = {} # Holds all item details
products = []
for item in names:
    parts = item.get_text().partition('(')
    products.append(parts[0])
    basket[parts[0]] = {} #Add the product name to dictionary as key to empty dict.


priceList = []
for price in prices:
    priceList.append(price.get_text())

#WIP
for i, product in enumerate(products):
    basket[product]["price"] = priceList[i] #Match prices to products
    if(i>20):
        break


#for keys in basket.keys():
#    print(basket.get(keys))
