import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("home-espresso-machines") +\
        get_sale_items_for("home-coffee-grinders") +\
        get_sale_items_for("home-coffee-brewers") +\
        get_sale_items_for("coffee-espresso-accessories")

def get_sale_items_for(page_type):
    base_url = f"https://caffetech.com/collections/{page_type}"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    website = 'caffetech.com'

    pages = soup.select('ul.pagination__nav a')
    if pages:
        num_pages = int(pages[-1].text)
    else:
        num_pages = 1

    sale_items = []

    for page_num in range(1,num_pages+1):
        if page_num > 1:
            page = requests.get(f"{base_url}?page={page_num}")
            soup = BeautifulSoup(page.content, 'html.parser')

        sale_prices = soup.select('span.product-item__price--new')
        for sale_price in sale_prices:
            sale_item = {
                'name' : f"{sale_price.parent.select('h4')[0].text.strip()} - {sale_price.parent.select('a')[0].text.strip()}",
                'image' : f"https:{sale_price.parent.parent.select('img')[1]['src'].strip()}",
                'url' : f"http://caffetech.com{sale_price.parent.select('a')[0]['href'].strip()}",
                'regular_price' : scanutil.get_money(sale_price.parent.select('span.product-item__price--old')[0].text),
                'sale_price' : scanutil.get_money(sale_price.text),
                'website' : website
            }
            sale_items.append(sale_item)

    return sale_items