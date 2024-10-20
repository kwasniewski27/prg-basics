hhmm = input('Enter time (24h time format): ')
h = hhmm[0:2]
m = hhmm[3:5]
h = int(h)
ampm = ""
if h > 12:
    h = h - 12
    h = str(h)
    ampm = h + ':' + m +" pm"
elif h <= 12:
    h = str(h)
    ampm = h + ':' + m + " am"
print(f'Time in 12=hour format: {ampm}')