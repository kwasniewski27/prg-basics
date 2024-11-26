hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
def hotel_list(hotels):
    for i in hotels:
        print(f'{i['name']}', end=',')
def avg_price(hotels):
    total = 0
    for x in hotels:
        if x['price']:
            total += x['price']
            average =  round(total/len(hotels))
    return average
hotel_list(hotels_in_Krakow)
print()
print(f"Average price of hotel in Krakow is {avg_price(hotels_in_Krakow)}")
print()
hotel_list(hotels_in_Sopot)
print()
print(f"Average price of hotels in Sopot is {avg_price(hotels_in_Sopot)}")
print()
if avg_price(hotels_in_Krakow)>avg_price(hotels_in_Sopot):
    print(f'Cheapest hotels are in Sopot')
else:
    print(f'Cheapest hotels are in: Krakow')