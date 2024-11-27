import json
with open('reservations.json', 'r', encoding='utf-8') as file:
    reservations = json.load(file)
room_count = 0
paid_reservations = 0
unpaid_reservations = 0
total_value_paid = 0
total_value_unpaid = 0
rooms = set()
for reservation in reservations:
    if 'room_number' in reservation:
        rooms.add(reservation["room_number"])
    if reservation['paid'] == True:
        paid_reservations += 1
        total_value_paid += int(reservation['nights'])*int(reservation['price_per_night'])
    elif reservation['paid'] == False:
        unpaid_reservations += 1
        total_value_unpaid += int(reservation['nights'])*int(reservation['price_per_night'])
room_count = len(rooms)
print('Total number of rooms is: ', room_count)
print('Number of paid reservations is: ', paid_reservations)
print('Number of unpaid reservations is: ', unpaid_reservations)
print('Total value of paid reservations is: ', total_value_paid)
print('Total value of unpaid reservations is: ', total_value_unpaid)