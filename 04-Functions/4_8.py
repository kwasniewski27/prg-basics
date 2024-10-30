def time_string(hours, minutes, time_format):
    if time_format == '24':
        time =  f'{hours:02}:{minutes:02}'
        return time
    elif time_format == '12':
        if hours == 0:
            hours_12 = 12
            am_pm = "AM"
        elif hours < 12:
            hours_12 = hours
            am_pm = "AM"
        elif hours >=12:
            hours_12 = hours - 12
            am_pm = "PM"
    time = (f'{hours_12}:{minutes:02}{am_pm}')
    return time
print(time_string(15,38,'24'))
print(time_string(8,3,'24'))
print(time_string(7,56,'24'))
print(time_string(19,2,'12'))