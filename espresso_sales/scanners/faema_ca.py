import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("espresso-machine", "category-s/1915.htm") +\
        get_sale_items_for("accessories", "Coffee-Accessories-s/1514.htm")


def get_sale_items_for(page_type, url_fragment):
    base_url = f"https://www.faema.ca/{url_fragment}?searching=Y&sort=13&cat=1915&show=1000&page=1"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    website = 'faema.ca'

    sale_items = []

    sale_prices = soup.select('div.product_saleprice')
    for sale_price in sale_prices:
        sale_item = {
            'name' : sale_price.parent.parent.parent.parent.parent.select('a')[0]['title'].strip(),
            'image' : f"https://faema.ca{sale_price.parent.parent.parent.parent.parent.select('img')[0]['src'].strip()}",
            'url' : sale_price.parent.parent.parent.parent.parent.select('a')[0]['href'].strip(),
            'regular_price' : scanutil.get_money(sale_price.parent.parent.parent.select('div.product_productprice')[0].text),
            'sale_price' : scanutil.get_money(sale_price.text),
            'website' : website
        }
        sale_items.append(sale_item)
        
    return sale_items