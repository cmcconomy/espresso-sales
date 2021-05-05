import json
from datetime import datetime, timezone
from concurrent.futures import ProcessPoolExecutor

from scanners import espressocanada_ca, \
    espressoplanet_ca, idrinkcoffee_com, espressodolce_ca, \
    faema_ca, caffetech_com, zcafe_ca, espressotec_com, \
    consiglioskitchenware_com, greenbeanery_ca, \
    wholelattelove_ca, homecoffeesolutions_com


def get_all_sales():

    with ProcessPoolExecutor() as executor:
        a01 = executor.submit(espressocanada_ca.get_sale_items)
        a02 = executor.submit(espressoplanet_ca.get_sale_items)
        a03 = executor.submit(idrinkcoffee_com.get_sale_items)
        a04 = executor.submit(espressodolce_ca.get_sale_items)
        a05 = executor.submit(faema_ca.get_sale_items)
        a06 = executor.submit(caffetech_com.get_sale_items)
        a07 = executor.submit(zcafe_ca.get_sale_items)
        a08 = executor.submit(espressotec_com.get_sale_items)
        a09 = executor.submit(consiglioskitchenware_com.get_sale_items)
        a10 = executor.submit(greenbeanery_ca.get_sale_items)
        a11 = executor.submit(wholelattelove_ca.get_sale_items)
        a12 = executor.submit(homecoffeesolutions_com.get_sale_items)

        sale_items = a01.result()+a02.result()+a03.result()+ \
                     a04.result()+a05.result()+a06.result()+ \
                     a07.result()+a08.result()+a09.result()+ \
                     a10.result()+a11.result()+a12.result()

    return {
        'retrieved_at' : datetime.now().replace(tzinfo=timezone.utc).astimezone(tz=None)
.strftime("%Y-%m-%d"),
        'sale_items' : sale_items
    }

if __name__ == "__main__":
    print( json.dumps(get_all_sales() ) )