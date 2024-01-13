def delivery_coordinate_maker():
    delivery_pt_names = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    delivery_pt_values = []
    lat_addition = 1.5 / 110692.0702932625
    long_addition = 1.5 / 105292.0089353767

    key_val = 0
    for i in range(3):
        for j in range(3):
            delivery_pt_values.append(
                tuple(
                    [
                        18.9998102845 + (i * lat_addition),
                        72.000142461 + (j * long_addition),
                        16.757981,
                    ]
                )
            )
            key_val += 1

    delivery_dict = dict(zip(delivery_pt_names, delivery_pt_values))
    return delivery_dict


def return_coordinate_maker():
    return_pt_names = ["X1", "X2", "X3", "Y1", "Y2", "Y3", "Z1", "Z2", "Z3"]
    return_pt_values = []
    lat_addition = 1.5 / 110692.0702932625
    long_addition = 1.5 / 105292.0089353767

    key_val = 0
    for i in range(3):
        for j in range(3):
            return_pt_values.append(
                tuple(
                    [
                        18.9999367615 + (i * lat_addition),
                        72.000142461 + (j * long_addition),
                        16.757981,
                    ]
                )
            )
            key_val += 1

    return_dict = dict(zip(return_pt_names, return_pt_values))
    return return_dict


delivery_grid = delivery_coordinate_maker()
return_grid = return_coordinate_maker()
print(delivery_grid)
print(return_grid)
