import time
hour_24time = input('Enter time (24h-hour format): ')
if hour_24time > 12:
    hour_12time = hour_24time - 12 
elif hour_24time <=12:
    hour_12time = hour_24time
print(f'Time in 24h format : {hour_24time}')
print(f'Time in 12h format: {hour_12time}')