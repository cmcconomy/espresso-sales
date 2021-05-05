import requests
from bs4 import BeautifulSoup
import scanutil
import re

def get_sale_items():
    return \
        get_sale_items_for("home-machines") +\
        get_sale_items_for("home-grinders.html")


def get_sale_items_for(page_type):
    base_url = f"https://www.espressotec.com/{page_type}?sort=pricedesc&limit=100&mode=4"
    soup = scanutil.get_soup(base_url)
    website = 'espressotec.com'

    sale_items = []

    sale_tags = soup.select('span.sale-text')
    for sale_tag in sale_tags:
        sale_item = {
            'name' : sale_tag.parent.parent.parent.select('h4')[0].text.strip(),
            'image' : sale_tag.parent.parent.select('img')[0]['src'].strip(),
            'url' : sale_tag.parent.parent.select('a')[0]['href'].strip(),
            'regular_price' : scanutil.get_money(sale_tag.parent.parent.parent.select('span.price--non-sale')[0].text),
            'sale_price' : scanutil.get_money(sale_tag.parent.parent.parent.select('span.price--withoutTax')[0].text),
            'website' : website
        }
        sale_items.append(sale_item)
        
    return sale_items