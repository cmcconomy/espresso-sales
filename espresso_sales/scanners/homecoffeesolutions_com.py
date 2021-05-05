import requests
from bs4 import BeautifulSoup
import scanutil
import re

def get_money(text):
    return float(re.search('.*?(((\d+),)*(\d+)(\.\d+)?)',text).group(1).replace(',',''))

def get_sale_items():
    return \
        get_sale_items_for("espresso-machines") +\
        get_sale_items_for("super-automatic-espresso-machines") +\
        get_sale_items_for("drip-coffee-makers") +\
        get_sale_items_for("coffee-grinders") +\
        get_sale_items_for("pour-over-coffee-makers")

def get_sale_items_for(page_type):
    base_url = f"https://www.homecoffeesolutions.com/collections/{page_type}"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    website = 'homecoffeesolutions.com'

    pages = soup.select('div.pagination__nav a')
    if pages:
        num_pages = int(int(pages[-1].text) / 2)
        # Why is it double???
    else:
        num_pages = 1
    
    sale_items = []

    for page_num in range(1,num_pages+1):
        if page_num > 1:
            page = requests.get(f"{base_url}?page={page_num}")
            soup = BeautifulSoup(page.content, 'html.parser')

        sale_prices = soup.select('span.price--highlight')
        for sale_price in sale_prices:

            sale_item = {
                'name' : sale_price.parent.parent.select('a')[0].text.strip(),
                'image' : f"https{sale_price.parent.parent.parent.parent.select('img')[0]['src'].strip()}",
                'url' : f"https://homecoffeesolutions.com{sale_price.parent.parent.select('a')[0]['href'].strip()}",
                'regular_price' : scanutil.get_money(sale_price.parent.parent.select('span.price--compare')[0].text),
                'sale_price' : scanutil.get_money(sale_price.text),
                'website' : website
            }
            sale_items.append(sale_item)

    return sale_items