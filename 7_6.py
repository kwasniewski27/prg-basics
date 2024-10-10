car_speed = input('Enter vehicle speed: ')
car_speed_valid = car_speed > "40" and car_speed < "140"
speed_not_valid = car_speed > "140" or car_speed < "40"
print(f'vehicle speed is valid', {car_speed_valid})
print(f'vehicle speed not valid', {speed_not_valid})