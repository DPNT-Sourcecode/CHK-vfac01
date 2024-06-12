

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    special_offers = {
        'A': {'count': 3, 'price': 130},
        'B': {'count': 2, 'price': 45}
    }

    if not all(sku in price_table for sku in skus):
        return -1

    total_cost = 0
    sku_counts = {}
    for sku in skus:
        sku_counts[sku] = sku_counts.get(sku, 0) + 1
          
    for sku, count in sku_counts.items():
        if sku in special_offers:
            special_offer = special_offers[sku]
            num_special_offers = count // special_offer['count']
            remaining_items = count % special_offer['count']
            total_cost += num_special_offers * special_offer['price']
            total_cost += remaining_items * price_table[sku]
        else:
            total_cost += count * price_table[sku]

    return total_cost
