import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    base_url = "https://wholelattelove.ca/collections/all-coffee-makers?_=pf"
    soup = scanutil.get_soup(base_url)
    website = 'wholelattelove.ca'

    sale_items = []

    page_num=1
    while True:
        if page_num > 1:
            soup = scanutil.get_soup(f"{base_url}&page={page_num}")

        if len(soup.select('div.product-wrap')) == 0:
            break
            
        sale_spans = soup.select('span.sale')
        for sale_span in sale_spans:
            if sale_span.parent.select('span.sold_out'):
                continue

            sale_item = {
                'name' : sale_span.parent.select('h2')[0].text.strip(),
                'image' : f"https:{sale_span.parent.parent.parent.select('img')[0]['data-src'].strip()}",
                'url' : f"https://wholelattelove.ca{sale_span.parent.parent.parent.select('a')[0]['href'].strip()}",
                'regular_price' : scanutil.get_money(sale_span.select('span.money')[1].text),
                'sale_price' : scanutil.get_money(sale_span.select('span.money')[0].text),
                'website' : website
            }
            sale_items.append(sale_item)
            
        page_num += 1

    return sale_items
