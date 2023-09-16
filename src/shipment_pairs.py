

# FIELDS: ORIGIN, DESTINATION, QUANTITY
SHIPMENTS = [
    ['US', 'US', 8],
    ['US', 'IN', 14],
    ['US', 'CA', 4],
    ['US', 'MX', 7],
    ['US', 'VE', 13],
    ['IN', 'US', 3],
    ['IN', 'IN', 13],
    ['IN', 'CA', 18],
    ['IN', 'MX', 16],
    ['IN', 'VE', 3],
    ['CA', 'US', 8],
    ['CA', 'IN', 20],
    ['CA', 'CA', 16],
    ['CA', 'MX', 3],
    ['CA', 'VE', 2],
    ['MX', 'US', 12],
    ['MX', 'IN', 20],
    ['MX', 'CA', 3],
    ['MX', 'MX', 3],
    ['MX', 'VE', 8],
    ['VE', 'US', 3],
    ['VE', 'IN', 7],
    ['VE', 'CA', 5],
    ['VE', 'MX', 15],
    ['VE', 'VE', 13],
 ]

def remove_intra(shipments):
    """remove_intra removes any records in which the origin and destination are the
    same country.

    Args:
        shipments (list): List of shipments with format [ORIGIN, DESTINATION, QUANTITY].

    Returns:
        list: List of shipments with intra-country shipments removed.
    """
    return [shipment for shipment in shipments if shipment[0] != shipment[1]]


def collect_pairs(shipments):
    """collect_pairs collects shipments for each unique country pair on one row.
    Note: the entire data set should be sorted on shipment count--largest first.

    The resulting fields (since origin and destinations are on the same row) will
    be:
        COUNTRY_A, COUNTRY_B, QUANTITY_AB, QUANTITY_BA

    Args:
        shipments (list): List of shipments with format [ORIGIN, DESTINATION, QUANTITY].

    Returns:
        list: List of collected pairs with format [COUNTRY_A, COUNTRY_B, QUANTITY_AB, QUANTITY_BA].
    """
    shipment_pairs = {}
    
    for shipment in shipments:
        origin, destination, quantity = shipment
        pair = (origin, destination)
        
        if pair not in shipment_pairs and (destination, origin) not in shipment_pairs:
            shipment_pairs[pair] = [quantity, 0]
        elif pair in shipment_pairs:
            shipment_pairs[pair][0] += quantity
        else:
            shipment_pairs[(destination, origin)][1] += quantity
    
    sorted_pairs = sorted(shipment_pairs.items(), key=lambda x: x[1][0], reverse=True)
    
    return [[pair[0][0], pair[0][1], pair[1][0], pair[1][1]] for pair in sorted_pairs]


if __name__ == '__main__':

    # Part 1
    export_only = remove_intra(SHIPMENTS)
    print('#' * 80, ' ' * 30 + 'Intra Removed', '#' * 80, sep='\n')
    print(export_only)

    # Part 2
    shipment_pairs = collect_pairs(SHIPMENTS)
    print('\n', '#' * 80, ' ' * 30 + 'Pairs collected', '#' * 80, sep='\n')
    print(shipment_pairs)
