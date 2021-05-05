import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("") +\
        get_sale_items_for("grinders/") +\
        get_sale_items_for("accessories/") +\
        get_sale_items_for("coffee-and-tea") +\
        get_sale_items_for("specials")

def get_sale_items_for(page_type):
    base_url = f"https://espressodolce.ca/product-category/espresso-machines/{page_type}/"
    soup = scanutil.get_soup(base_url)
    website = 'espressodolce.ca'

    pages = soup.select('ul.page-numbers a')
    if pages:
        num_pages = len(pages)
    else:
        num_pages = 1

    sale_items = []

    for page_num in range(1,num_pages+1):
        if page_num > 1:
            soup = scanutil.get_soup(f"{base_url}/page/{page_num}")
        
        orig_prices = soup.select('del')

        for orig_price in orig_prices:
            sale_item = {
                'name' : orig_price.parent.parent.select('p.name')[0].text.strip(),
                'image' : orig_price.parent.parent.parent.parent.select('img')[0]['src'].strip(),
                'url' : orig_price.parent.parent.select('a')[1]['href'].strip(),
                'regular_price' : scanutil.get_money(orig_price.text),
                'sale_price' : scanutil.get_money(orig_price.parent.select('ins')[0].text),
                'website' : website
            }
            sale_items.append(sale_item)

    return sale_items