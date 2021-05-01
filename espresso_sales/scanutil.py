import re

def get_money(text):
    return float(re.search('.*?(((\d+),)*(\d+)(\.\d+)?)',text).group(1).replace(',',''))
