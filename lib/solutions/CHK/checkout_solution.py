

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    special_offers = {
        'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
        'B': [{'count': 2, 'price': 45}],
        'E': [{'count': 2, 'free_item': 'B', 'free_count': 1}],
    }

    if not all(sku in price_table for sku in skus):
        return -1

    total_cost = 0
    sku_counts = {}
    for sku in skus:
        sku_counts[sku] = sku_counts.get(sku, 0) + 1
          
    if 'E' in sku_counts and 'E' in special_offers:
        offer = special_offers['E'][0]
        count_E = sku_counts['E']
        free_B_count = (count_E // offer['count']) * offer['free_count']
        if 'B' in sku_counts:
            sku_counts['B'] = max(sku_counts['B'] - free_B_count, 0)
          
    for sku, count in sku_counts.items():
        if sku in special_offers:
            for special_offer in sorted(special_offers[sku], key=lambda x: x['count'], reverse=True):
                if 'price' in special_offer:
                    num_special_offers = count // special_offer['count']
                    remaining_items = count % special_offer['count']
                    total_cost += num_special_offers * special_offer['price']
                    count = remaining_items
            total_cost += count * price_table[sku]
        else:
            total_cost += count * price_table[sku]

    return total_cost
