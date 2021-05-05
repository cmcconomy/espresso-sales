import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("espresso-machine") +\
        get_sale_items_for("coffee-maker") +\
        get_sale_items_for("grinder") +\
        get_sale_items_for("accessories") +\
        get_sale_items_for("open-box-returns")

def get_sale_items_for(page_type):
    if page_type != "open-box-returns":
        page_type = f"consumer/{page_type}" 

    base_url = f"https://idrinkcoffee.com/collections/{page_type}"
    soup = scanutil.get_soup(base_url)
    website = 'idrinkcoffee.com'

    pages = soup.select('div.articlePreviewPagination a')
    if pages:
        num_pages = int(pages[-1].text)
    else:
        num_pages = 1

    sale_items = []
    for page_num in range(1,num_pages+1):
        if page_num > 1:
            soup = scanutil.get_soup(f"{base_url}?page={page_num}")
        
        orig_prices = soup.select('s')
        for orig_price in orig_prices:
            sale_item = {
                'name' : orig_price.parent.parent.select('h2')[0].text.strip(),
                'image' : f"https:{orig_price.parent.parent.select('img')[0]['data-src'].strip()}",
                'url' : f"https://www.idrinkcoffee.com/{orig_price.parent.parent['href'].strip()}",
                'regular_price' : scanutil.get_money(orig_price.text),
                'sale_price' : scanutil.get_money(orig_price.parent.select('span')[0].text),
                'website' : website
            }
            sale_items.append(sale_item)

    return sale_items
