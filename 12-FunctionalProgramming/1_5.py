distance = int(input('Enter your distance in km: '))
hours = int(input('Enter your travel hours: '))
minutes = int(input('Enter your travel minutes: '))
def avg_speed(distance,hours,minutes):
    result = (distance)/(hours+minutes/60)
    result = round(result, 2)
    return result
print(f'Average speed: {avg_speed(distance, hours, minutes)} km/h')