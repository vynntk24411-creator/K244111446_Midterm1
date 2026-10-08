BASE_PRICE = 100000
DA_LAT_DISCOUNT = 0.15


def calc_da_lat_revenue(quantity):
    price = BASE_PRICE * (1 - DA_LAT_DISCOUNT)
    revenue = quantity * price
    return revenue


def calc_sapa_revenue(quantity):
    revenue = quantity * BASE_PRICE
    return revenue


def calc_total_revenue(da_lat_revenue, sapa_revenue):
    total = da_lat_revenue + sapa_revenue
    return total