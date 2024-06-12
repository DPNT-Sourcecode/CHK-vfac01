

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    sorted_price_table = {k: v for k, v in sorted(price_table.items(), key=lambda item: item[1], reverse=True)}

    special_offers = {
        'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
        'B': [{'count': 2, 'price': 45}],
        'E': [{'count': 2, 'free_item': 'B', 'free_count': 1}],
        'F': [{'count': 3, 'price': 20}],
        'H': [{'count': 10, 'price': 80}, {'count': 5, 'price': 45}],
        'K': [{'count': 2, 'price': 150}],
        'N': [{'count': 3, 'free_item': 'M', 'free_count': 1}],
        'P': [{'count': 5, 'price': 200}],
        'Q': [{'count': 3, 'price': 80}],
        'R': [{'count': 3, 'free_item': 'Q', 'free_count': 1}],
        'U': [{'count': 4, 'price': 120}],
        'V': [{'count': 3, 'price': 130}, {'count': 2, 'price': 90}],
        'S': [],
        'T': [],
        'X': [],
        'Y': [],
        'Z': []
    }

    group_discount_items = {'S', 'T', 'X', 'Y', 'Z'}
    group_discount_price = 45

    group_discount_skus = ''.join([sku for sku in skus if sku in group_discount_items])
    print(group_discount_skus)
    sorted_group_discount_skus = ''.join(sorted(group_discount_skus, key=lambda sku:sorted_price_table[sku], reverse=True))
    print(sorted_group_discount_skus)
    skus = sorted_group_discount_skus
    if not all(sku in price_table for sku in skus):
        return -1

    total_cost = 0
    sku_counts = {}
    for sku in skus:
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    group_discount_count = sum(sku_counts.get(item, 0) for item in group_discount_items)
    # print(group_discount_count)
    group_discount_application = group_discount_count // 3
    total_cost += group_discount_application * group_discount_price
    print(total_cost)
    if group_discount_application > 0:
        run_times = group_discount_application * 3
        for sku in skus :
            if sku in group_discount_items:
                if sku in sku_counts:
                    print(f"Hellow = {sku}")
                    total_cost -= price_table[sku]
                    run_times -= 1
                    if run_times == 0:
                        break

    for sku, offers in special_offers.items():
        for offer in offers:
            if 'free_item' in offer and sku in sku_counts:
                free_item_count = (sku_counts[sku] // offer['count']) * offer['free_count']
                if offer['free_item'] in sku_counts:
                    sku_counts[offer['free_item']] = max(sku_counts[offer['free_item']] - free_item_count, 0)
          
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




