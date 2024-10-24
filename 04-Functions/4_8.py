import time

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        if hours >= 12:
            period = "PM"
            hour_12 = hours - 12
        elif hours <12:
            period = "AM" 
            hour_12 = hours
        return f"{hour_12}:{minutes:02} {period}"
    else:
        return "Invalid time format"
print(time_string(15, 38, '24')),  
print(time_string(8, 3, '24')),    
print(time_string(0, 5, '24')),  
print(time_string(11, 15, '12')),    
print(time_string(19, 2, '12')),  
print(time_string(0, 7, '12')),  
print(time_string(7, 30, '12')),   
print(time_string(13, 10, '12')),   
print(time_string(12, 46, '12')),   