from scanners import espressocanada_ca, espressoplanet_ca


def get_all_sales():
    return \
        espressocanada_ca.get_sale_items() + \
        espressoplanet_ca.get_sale_items()

print("hello")

print( get_all_sales() )