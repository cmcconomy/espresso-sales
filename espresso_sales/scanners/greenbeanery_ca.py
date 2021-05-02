import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("grinders") +\
        get_sale_items_for("espresso-machines-c-35")


def get_sale_items_for(page_type):
    base_url = f"https://greenbeanery.ca/collections/{page_type}"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    website = 'greenbeanery.ca'

    sale_items = []

    sale_spans = soup.select('span.sale')
    for sale_span in sale_spans:
        
        if sale_span.parent.select('span.sold_out'):
            continue
        
        sale_item = {
            'name' : sale_span.parent.select('span.title')[0].text.strip(),
            'image' : f"https:{sale_span.parent.parent.parent.select('img')[0]['data-src'].strip()}",
            'url' : f"https://greenbeanery.ca{sale_span.parent.parent.parent.select('a')[0]['href'].strip()}",
            'regular_price' : scanutil.get_money(sale_span.select('span.money')[1].text),
            'sale_price' : scanutil.get_money(sale_span.select('span.money')[0].text),
            'website' : website
        }
        sale_items.append(sale_item)
        
    return sale_items