import requests
from bs4 import BeautifulSoup
import scanutil

def get_sale_items():
    return \
        get_sale_items_for("espresso") + \
        get_sale_items_for("grinders")

def get_sale_items_for(page_type):
    if page_type == "espresso":
        base_url = "https://www.espressoplanet.com/coffee-espresso/espresso-machines/?sort=orderby&sort_direction=0&objects_per_page=1000"
    elif page_type == "grinders":
        base_url = "https://www.espressoplanet.com/coffee-espresso/coffee-grinder/?sort=orderby&sort_direction=0&objects_per_page=1000"
    else:
        return []

    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
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