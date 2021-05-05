import json
import datetime
from scanners import espressocanada_ca, \
    espressoplanet_ca, idrinkcoffee_com, espressodolce_ca, \
    faema_ca, caffetech_com, zcafe_ca, espressotec_com, \
    consiglioskitchenware_com, greenbeanery_ca, \
    wholelattelove_ca, homecoffeesolutions_com


def get_all_sales():
    sale_items = \
        espressocanada_ca.get_sale_items() + \
        espressoplanet_ca.get_sale_items() + \
        idrinkcoffee_com.get_sale_items() + \
        espressodolce_ca.get_sale_items() + \
        faema_ca.get_sale_items() + \
        caffetech_com.get_sale_items() + \
        zcafe_ca.get_sale_items() + \
        espressotec_com.get_sale_items() + \
        consiglioskitchenware_com.get_sale_items() + \
        greenbeanery_ca.get_sale_items() + \
        wholelattelove_ca.get_sale_items() + \
        homecoffeesolutions_com.get_sale_items()

    return {
        'retrieved_at' : datetime.datetime.now().strftime("%Y-%m-%d"),
        'sale_items' : sale_items
    }

if __name__ == "__main__":
    print( json.dumps(get_all_sales() ) )