import sys
from bs4 import BeautifulSoup
import urllib.request
import os, csv, json

url = 'http://www.mysupermarket.co.uk/shelf/top_offers_from_across_the_uk'
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser') # Get the soup

items = soup.find_all('li', id='NgMspProductCell') # Find all listed items on page
names = soup.select('div[class=DetailsWrp] h3 a span') # Traverse the elements in the listed items

basket = {} # Holds all item details
for item in names:
    parts = item.get_text().partition('(')
    basket[parts[0]] = {}
