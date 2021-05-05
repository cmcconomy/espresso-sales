import re
import time
import requests
from bs4 import BeautifulSoup

def get_money(text):
    return float(re.search('.*?(((\d+),)*(\d+)(\.\d+)?)',text).group(1).replace(',',''))

def get_soup(url, max_tries=5, sleep_secs=5, timeout=20):
    tries = 0
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    while tries < max_tries:
        try: 
            page = requests.get(url, headers=headers, timeout=timeout)
            break
        except Exception as e:
            time.sleep(sleep_secs)
            tries += 1
            continue

    if tries == max_tries:
        print(f"Failed {tries} times to retrieve {url}")
    return BeautifulSoup(page.content, 'html.parser')