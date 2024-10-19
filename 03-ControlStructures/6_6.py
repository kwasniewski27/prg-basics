time = int(input('Enter time: '))
if time == 1 or time == 2:
    value = '5 PLN'
elif time == 3 or time == 4 or time == 5 or time == 6:
    value = '15 PLN'
elif time > 6:
    value = '20 PLN'
elif time < 0:
    print('something went wrong')
print(f'you have to pay {value} for parking')