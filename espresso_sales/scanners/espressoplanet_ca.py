import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("espresso-machines") + \
        get_sale_items_for("grinders") + \
        get_sale_items_for("coffee-maker") + \
        get_sale_items_for("accessories")

def get_sale_items_for(page_type):
    base_url = f"https://www.espressoplanet.com/coffee-espresso/{page_type}/?sort=orderby&sort_direction=0&objects_per_page=1000"
    soup = scanutil.get_soup(base_url)
    website = 'espressoplanet.com'

    market_price_values = soup.select('span.market-price-value')

    sale_items = []
    for market_price_value in market_price_values:
        sale_item = {
            'name' : market_price_value.parent.parent.parent.select('a')[0].text.strip(),
            'image' : market_price_value.parent.parent.parent.parent.select('img')[0]['data-src'].strip(),
            'url' : f"https://www.espressoplanet.com/{market_price_value.parent.parent.parent.select('a')[0]['href'].strip()}",
            'regular_price' : scanutil.get_money(market_price_value.text.strip()),
            'sale_price' : scanutil.get_money(market_price_value.parent.parent.select('span.currency')[0].text.strip()),
            'website' : website
        }
        sale_items.append(sale_item)

    return sale_items