import requests
from bs4 import BeautifulSoup

url = 'https://leagueoflegends.fandom.com'

response = requests.get(url+'/wiki/Item_(League_of_Legends)')

soup = BeautifulSoup(response.content, 'html.parser')

item_icons = soup.find_all("div", {"class": 'item-icon'})

item_template = {
    "name": "N/A",
    "price": 0,
    "stats": [],
    "id": 0
}

items = []

def find_item_id(item_soup):
    return item_soup.find('td', {"data-source": "id"}).contents

def find_item_price(item_soup):
    return item_soup.find('span', {"data-source": "buy"}).contents

for item in item_icons:

    # Create a new item object from our template
    new_item = item_template

    # Opening the item page and parsing the html
    item_link = item.find('a')
    item_response = requests.get(url+item_link.get('href'))
    item_soup = BeautifulSoup(item_response.content, 'html.parser')

    # set the name, id, and price values for our item
    new_item["name"] = item_soup.find('span', {'class': 'mw-page-title-main'}).contents
    new_item["price"] = find_item_price(item_soup)
    new_item["id"] = find_item_id(item_soup)
    print(new_item)


# item-grid -> item-icon ->

# soup.p['class']

