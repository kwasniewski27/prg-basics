car_speed = int(input('Enter your speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed < speed_limit_min:
    print('Warning: invalid car speed!!')
    print('Your speed is too low')
elif car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
    print('Your speed is too high')
else:
    print('Your speed is ok')
