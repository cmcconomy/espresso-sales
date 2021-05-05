import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("espresso-machines") +\
        get_sale_items_for("coffee-makers-grinders")

def get_sale_items_for(page_type):
    base_url = f"https://www.consiglioskitchenware.com/collections/{page_type}?view=view-48"
    soup = scanutil.get_soup(base_url)
    website = 'consiglioskitchenware.com'

    page_links = soup.select('a.pagination--item')
    if page_links:
        num_pages = len(page_links)
    else:
        num_pages = 1

    sale_items = []

    for page_num in range(1,num_pages+1):
        if page_num > 1:
            soup = scanutil.get_soup(f"{base_url}&page={page_num}")

        orig_prices = soup.select('div.price--compare-at')
        for orig_price in orig_prices:
            if orig_price.text.strip() == "" or orig_price.parent.parent.parent.select('a') == []:
                continue

            sale_item = {
                'name' : orig_price.parent.parent.select('h2')[0].text.strip(),
                'image' : f"https:{orig_price.parent.parent.parent.select('img')[0]['src'].strip()}",
                'url' : f"https://consiglioskitchenware.com{orig_price.parent.parent.select('a')[0]['href'].strip()}",
                'regular_price' : scanutil.get_money(orig_price.text),
                'sale_price' : scanutil.get_money(orig_price.parent.parent.select('div.price--main')[0].text),
                'website' : website
            }
            sale_items.append(sale_item)

    return sale_items