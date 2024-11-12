def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    if n==1:
        weekdays = weekdays[0]
    elif n==2:
        weekdays = weekdays[1]
    elif n==3:
        weekdays = weekdays[2]
    elif n==4:
        weekdays = weekdays[3]
    elif n==5:
        weekdays = weekdays[4]
    elif n==6:
        weekdays = weekdays[5]
    elif n==7:
        weekdays = weekdays[6]
    return n, weekdays
print(weekday(1))
print(weekday(4))
print(weekday(7))