car_number = input('Enter car registration number:')
is_krakow = str(car_number [0:2] == "KR" or car_number [0:2] == "KK" or car_number [0:2] == "kk" or car_number [0:2] == "kr")
isnt_krakow = str(car_number [0:2] != "KR" or "KK")
print(f'Car is from Krakow: {is_krakow}')
print(f'Car is not from Krakow: {isnt_krakow}')