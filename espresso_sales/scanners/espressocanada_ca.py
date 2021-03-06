import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    base_url = "https://espressocanada.com/collections/saeco-philips-and-jura-superautomatic-coffee-machines"
    soup = scanutil.get_soup(base_url)
    website = 'espressocanada.com'

    sale_spans = soup.select('span.sale')

    sale_items = []

    for sale_span in sale_spans:
        if sale_span.select('span.sold_out'):
            continue

        sale_item = {
            'type' : 'superauto',
            'name' : sale_span.parent.select('span.title')[0].text.strip(),
            'image' : f"https:{sale_span.parent.parent.parent.select('img.noscript')[0]['src'].strip()}",
            'url' : f"https://espressocanada.com{sale_span.parent.parent.parent.select('a')[0]['href'].strip()}",
            'regular_price' : scanutil.get_money(sale_span.select('span.was_price')[0].text),
            'sale_price' : scanutil.get_money(sale_span.select('span.money')[0].text),
            'website' : website
        }
        
        sale_items.append(sale_item)
        
    return sale_items
