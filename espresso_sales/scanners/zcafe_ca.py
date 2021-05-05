import requests
from bs4 import BeautifulSoup
import scanutil
import re

def get_sale_items():
    return \
        get_sale_items_for("home-sales", "SpecialList.aspx") +\
        get_sale_items_for("commercial-sales", "ProductListByCategoryID.aspx?ID=169")


def get_sale_items_for(page_type, url_fragment):
    base_url = f"https://www.zcafe.ca/site/{url_fragment}"
    soup = scanutil.get_soup(base_url)
    website = 'zcafe.ca'

    sale_items = []

    images = soup.select('img[style]')
    for image in images:
        url = image.parent.parent.select('a')[0]['href'].strip()
        img_src = re.search('.*\((.*)\).*',image['style']).group(1)
        sale_item = {
            'name' : image.parent.parent.parent.parent.select('a.producttitle')[0].text.strip(),
            'image' : f"https://zcafe.ca{img_src}",
            'url' : url,
            'regular_price' : get_regular_price(url),
            'sale_price' : scanutil.get_money(image.parent.parent.parent.parent.parent.select('div')[0].text),
            'website' : website
        }
        sale_items.append(sale_item)
        
    return sale_items

def get_regular_price(url):
    soup = scanutil.get_soup(url)
    price = scanutil.get_money(soup.select('#ProductInfo_Lbl_product_price_strike')[0].text)
    return price
